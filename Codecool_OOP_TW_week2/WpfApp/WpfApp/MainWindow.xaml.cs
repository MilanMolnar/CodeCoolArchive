using System;
using System.Windows;
using System.Windows.Input;
using System.Timers;
using System.Diagnostics;
using GetProcesses;


namespace WpfApp
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public static Processes currentProcessList = new Processes();
        public static int indexOfListItem;
        public static Timer timer = new Timer();
        public static bool onlineStaus = false;
        public MainWindow()
        {
            InitializeComponent();
        }

        private void ListProc(object sender, ElapsedEventArgs e)
        {
            
            Dispatcher.Invoke(() => {
                Start();
            });
        }
        private void Start()
        {
            //Starts the process calculation
            Process[] runningProcesses = Process.GetProcesses();
            currentProcessList.LocalAll.Clear();

            listBox.Items.Clear();
            foreach (var process in runningProcesses)
            {
                listBox.Items.Add("PID:".PadRight(6) + Convert.ToString(process.Id).PadRight(15 - Convert.ToString(process.Id).Length) + "Name:".PadRight(7) + Convert.ToString(process.ProcessName));
            }

            foreach (var item in runningProcesses)
            {
                var process = new Proc(item);
                currentProcessList.LocalAll.Add(process);
            }
            onlineStaus = true;
        }
        private void Save_Button_Click(object sender, RoutedEventArgs e)
        {
            if (switchBox.IsChecked == true)
            {
                Switchturn switchturn2 = new Switchturn();
                switchturn2.Show();
            }
            else
            {
                DataManager.Serial(currentProcessList.LocalAll);
                Serialized win3 = new Serialized();
                win3.Show();
            }
        }

        private void Run_Button_Click(object sender, RoutedEventArgs e)
        {
            if (switchBox.IsChecked == true)
            {
                Switchturn switchturn = new Switchturn();
                switchturn.Show();
            }
            else
            {
                Proc.RunNewProcess(runTextBox.Text);
                runTextBox.Clear();
            }
        }

        private void CheckBox_Checked(object sender, RoutedEventArgs e)
        {
            Start();
            DoEvents(true);
        }

        private void CheckBox_Unchecked(object sender, RoutedEventArgs e)
        {
            DoEvents(false);
        }

        protected void DoEvents(bool isOn)
        {
            if (isOn)
            {
                timer.Interval = (20 * 1000);
                timer.Elapsed += new ElapsedEventHandler(ListProc);
                timer.Start();
            }
            else
            {
                timer.Stop();
            }
       }
        private void Load_Button_Click(object sender, RoutedEventArgs e) 
        { 
            if (!switchBox.IsChecked == true)
            {
                onlineStaus = false;
                currentProcessList = new Processes();
                int longestId = -1;
                int longestName = -1;
                DataManager.DeSerial(currentProcessList);
                listBox.Items.Clear();
                foreach (var process in currentProcessList.LocalAll)
                {
                    if (Convert.ToString(process.Id).Length > longestId)
                    {
                        longestId = Convert.ToString(process.Id).Length;
                    }
                }
                foreach (var process in currentProcessList.LocalAll)
                {
                    if (process.Name.Length > longestName)
                    {
                        longestName = process.Name.Length;
                    }
                }
                foreach (var process in currentProcessList.LocalAll)
                {
                    if (!string.IsNullOrEmpty(process.Comment))
                    {
                        listBox.Items.Add("PID:".PadRight(6) + Convert.ToString(process.Id).PadRight(15 - Convert.ToString(process.Id).Length) +
                            "Name:".PadRight(7) + Convert.ToString(process.Name) + "    Comment:   " + Convert.ToString(process.Comment));
                    }
                    else
                    {
                        listBox.Items.Add("PID:".PadRight(6) + Convert.ToString(process.Id).PadRight(15 - Convert.ToString(process.Id).Length) + "Name:".PadRight(7) + Convert.ToString(process.Name));
                    }
                }
            }
            else
            {
                Switchturn switchwindow = new Switchturn();
                switchwindow.Show();
            }
        }
        private void ListItem_Button_Click(object sender, RoutedEventArgs e) 
        {
            if (!switchBox.IsChecked == true)
            {
                indexOfListItem = listBox.SelectedIndex;
                window2 win2 = new window2();
                win2.Show();
            }
            else
            {               
                Switchturn switchturn2 = new Switchturn();
                switchturn2.Show();
            }
            
        }

        private void Start_Button_Click(object sender, RoutedEventArgs e)
        {
            Start();
        }


        private void Kill_Button_Click(object sender, RoutedEventArgs e)
        {
            Proc.Kill();
        }

        private void runTextBox_KeyDown(object sender, KeyEventArgs e)
        {
            if (switchBox.IsChecked == true)
            {
                Switchturn switchturn = new Switchturn();
                switchturn.Show();
            }
            else
            {
                if (e.Key == Key.Return)
                {
                    Proc.RunNewProcess(runTextBox.Text);
                    runTextBox.Clear();
                }  
            }
        }
    }
}
