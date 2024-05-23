using System;
using System.Windows;
using System.Windows.Input;
using GetProcesses;

namespace WpfApp
{
    /// <summary>
    /// Interaction logic for window2.xaml
    /// </summary>
    public partial class window2 : Window
    {
        

        public window2()
        {
            var indexCurrentProc = MainWindow.currentProcessList.LocalAll[MainWindow.indexOfListItem];
            InitializeComponent();
            listBoxDetails.Items.Clear();
            if (MainWindow.onlineStaus && indexCurrentProc.Name != "Idles")
            {
                try
                {
                    var result = Proc.run_cmd(indexCurrentProc.Id);
                    indexCurrentProc.CpuUsage = Convert.ToDouble(result);
                }
                catch (Exception)
                {

                    Console.WriteLine();
                }
                
            }
            listBoxDetails.Items.Add($"CPU: {indexCurrentProc.CpuUsage}, Memory: {indexCurrentProc.MemoryUsage}, Threads: {indexCurrentProc.Threads}," +
                $" Start time: {indexCurrentProc.StartTime}, Run Time: {indexCurrentProc.RunningTime}");
            CommentText.Text = indexCurrentProc.Comment;
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            var indexCurrentProc = MainWindow.currentProcessList.LocalAll[MainWindow.indexOfListItem];
            string commentText = CommentText.Text;
            if (!string.IsNullOrEmpty(commentText))
            {
                indexCurrentProc.Comment = commentText;
            }
            Saved win3 = new Saved();
            win3.Show();
            this.Close();
        }

        private void CommentText_MouseDoubleClick(object sender, MouseButtonEventArgs e)
        {

        }
    }
}
