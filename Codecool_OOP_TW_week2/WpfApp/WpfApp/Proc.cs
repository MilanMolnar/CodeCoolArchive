using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Runtime.Serialization;
using System.Threading.Tasks;
using System.IO;

namespace GetProcesses
{
    [Serializable()]
    public class Proc 
    {

        public string Name;
        public int Id;
        public DateTime StartTime;
        public double CpuUsage;
        public double MemoryUsage;
        public TimeSpan RunningTime;
        public int Threads;
        public List<Proc> ProcList = new List<Proc>();
        public string Comment;

        public Proc() { }
        public Proc(Process process)
        {
            try
            {
                this.Name = process.ProcessName;
                this.Id = process.Id;
                this.StartTime = process.StartTime;
                this.RunningTime = DateTime.Now - StartTime;
                this.Threads = process.Threads.Count;
                this.MemoryUsage = Math.Round((double)process.WorkingSet64 / 1024 / 1024, 2);                
            }
            catch (Exception)
            {
                Console.WriteLine();
            }
        }

        public static void Kill()
        {
            Process[] runningProcesses = Process.GetProcesses();
            foreach (var process in runningProcesses)
            {
                try
                {
                    process.Kill();
                }
                catch (Exception)
                {
                    Console.WriteLine("I can't kill everything :(  " + process.ProcessName);
                }
            }
        }
        public static void RunNewProcess(string txtOpen)
        {
            if (!string.IsNullOrEmpty(txtOpen))
            {
                try
                {
                    Process proc = new Process();
                    proc.StartInfo.UseShellExecute = true;
                    proc.StartInfo.FileName = txtOpen;
                    proc.Start();
                }
                catch (Exception ex)
                {

                    Console.WriteLine(); 
                }
            }
        }
        public static string run_cmd(int args)
        {
            ProcessStartInfo start = new ProcessStartInfo
            {
                FileName = @"python",
                ArgumentList = { @"C:\Users\nevie\Desktop\XML_start\WpfApp\WpfApp\CPUusage.py", args.ToString() },
                RedirectStandardError = true,
                RedirectStandardOutput = true
            };
            using (Process process = Process.Start(start))
            {
                process.WaitForExit();
                var stderr = process.StandardError.ReadToEnd(); // Here are the exceptions from our Python script
                var result = process.StandardOutput.ReadToEnd(); // Here is the result of StdOut(for example: print "test")
                return result;
            }
        }
    }
}






