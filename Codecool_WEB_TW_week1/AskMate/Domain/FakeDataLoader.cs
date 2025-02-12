﻿using Microsoft.AspNetCore.Hosting;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace AskMate.Domain
{
    public class FakeDataLoader : IDataLoader
    {
        private List<Question> ListOfQuestions = new List<Question>();

        public FakeDataLoader()
        {
            LoadQuestion();
        }
        
        public int AddQuestion(string title, string text, string image)
        {
            int nextID;
            if (ListOfQuestions.Count == 0)
            {
                nextID = 1;
            }
            else
            {
                nextID = ListOfQuestions.Select(q => q.ID).Max() + 1;
            }
            ListOfQuestions.Add(new Question(nextID,title, text, image, DateTime.Now));
            WriteQuestionToCSV();
            WriteAnswerToCSV();
            return nextID;
        }


        public int CountAnswers(int questionId)
        {
            foreach (var question in ListOfQuestions)
            {
                if(question.ID.Equals(questionId))
                {
                    WriteQuestionToCSV();
                    WriteAnswerToCSV();
                    return question.ListOfAnswers.Count;
                }
            }
            return 0;
        }

        public Question GetQuestion(int questionId)
        {

            foreach (var question in ListOfQuestions)
            {
                if (question.ID.Equals(questionId))
                {
                    WriteQuestionToCSV();
                    WriteAnswerToCSV();
                    return question;
                }
            }
            return null;
        }

        public List<Question> GetQuestions()
        {
            return ListOfQuestions;
        }



        public int AddComment(int questionID,string message,string image)
        {
            int nextID = 0;
            foreach (var q in ListOfQuestions)
            {
                if (q.ListOfAnswers.Count == 0)
                {
                    nextID = 1;
                }
                else
                {
                    nextID = q.ListOfAnswers.Select(aq => q.ID).Max() + 1;
                }
            }


            foreach (var q in ListOfQuestions)
            {
                if (q.ID.Equals(questionID))
                {
                    q.ListOfAnswers.Add(new Answer(nextID, message,questionID,image,DateTime.Now));
                    q.NumOfMessages++;
                    WriteQuestionToCSV();
                    WriteAnswerToCSV();
                    return nextID;

                }
            }
            throw new Exception("There is no such ID");
            
        }

        public void DeleteQuestion(int ID)
        {
            for (int i = 0; i < ListOfQuestions.Count; i++)
            {
                if (ListOfQuestions[i].ID == ID)
                {
                    ListOfQuestions.Remove(ListOfQuestions[i]);
                }
            }
            WriteQuestionToCSV();
            WriteAnswerToCSV();
        }

        public void DeleteComment(int ID)
        {

            foreach (var q in ListOfQuestions)
            {
                foreach (var answer in q.ListOfAnswers)
                {
                    if (answer.ID == ID)
                    {
                        q.ListOfAnswers.Remove(answer);
                        q.NumOfMessages--;
                        return;
                    }
                }
            }
            WriteQuestionToCSV();
            WriteAnswerToCSV();
        }

        public void EditQuestion(int qid,string title, string text)
        {
            foreach (var q in ListOfQuestions)
            {
                if (q.ID == qid)
                {
                    if (title != q.Title & title != null)
                    {
                        q.Title = title;
                    }

                    if (text != q.Text & text != null)
                    {
                        q.Text = text;
                    }
                }
            }
            WriteQuestionToCSV();
            WriteAnswerToCSV();
        }
        public void Like(int qid)
        {
            foreach (var q in ListOfQuestions)
            {
                if(q.ID == qid)
                {
                    q.Like++;
                }
            }
            WriteQuestionToCSV();
            WriteAnswerToCSV();
        }
        public void Dislike(int qid)
        {
            foreach (var q in ListOfQuestions)
            {
                if (q.ID == qid)
                {
                    q.Dislike++;
                }
            }
            WriteQuestionToCSV();
            WriteAnswerToCSV();
        }

        public void LikeAnswer(int aid,int qid)
        {
            foreach (var q in ListOfQuestions)
            {
                if (q.ID == qid)
                {
                    foreach (var an in q.ListOfAnswers)
                    {
                        if (aid == an.ID)
                        {
                            an.UpVotes++;
                        }
                    }
                }
            }
            WriteQuestionToCSV();
            WriteAnswerToCSV();
        }
        public void DislikeAnswer(int aid,int qid)
        {

            foreach (var q in ListOfQuestions)
            {
                if (q.ID == qid)
                {
                    foreach (var an in q.ListOfAnswers)
                    {
                        if (aid == an.ID)
                        {
                            an.DownVotes++;
                        }
                    }
                }
            }
            WriteQuestionToCSV();
            WriteAnswerToCSV();
        }
        
        public void WriteQuestionToCSV()
        {
            string questionDatabase = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "QuestionDatabase.csv");
            using (var w = new StreamWriter(questionDatabase))
            {
                for (int i = 0; i < ListOfQuestions.Count; i++)
                {
                    var q = ListOfQuestions[i];
                    if (string.IsNullOrEmpty(q.Image))
                    {
                        q.Image = "";
                    }
                   
                    w.WriteLine($"{q.ID},{q.Title},{q.Text},{q.Image},{q.Like},{q.Dislike},{q.NumOfMessages},{q.NumOfViews},{q.PostedDate}");
                    w.Flush();
                }
            }
        }

        public void WriteAnswerToCSV()
        {
            string questionDatabase = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "AnswerDatabase.csv");
            using (var w = new StreamWriter(questionDatabase))
            {
                foreach (var q in ListOfQuestions)
                {
                    foreach (var a in q.ListOfAnswers)
                    {
                        if(string.IsNullOrEmpty(a.Image))
                        {
                            a.Image = "";
                        }
                        w.WriteLine($"{q.ID},{a.ID},{a.Text},{a.Image},{a.UpVotes},{a.DownVotes},{a.PostedDate}");
                        w.Flush();
                    }

                }
            }
        }
        public List<Question> LoadQuestion()
        {
            string questionDatabase = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "QuestionDatabase.csv");
            string answerDatabase = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "AnswerDatabase.csv");
            string[] lines = File.ReadAllLines(questionDatabase);
            string[] anslines = File.ReadAllLines(answerDatabase);
            Regex CSVParser = new Regex(",");
            Regex AnsParser = new Regex(",");
            int rowcount = 0;
            foreach (var row in lines)
            {
                
                Question q = new Question();
                String[] Fields = CSVParser.Split(row);
                for (int i = 0; i < Fields.Length; i++)
                {
                    Fields[i] = Fields[i].TrimStart(' ', '"');
                    Fields[i] = Fields[i].TrimEnd('"');
                }
                q.ID = int.Parse(Fields[0]);
                q.Title = Fields[1];
                q.Text = Fields[2];
                if(Fields[3]!= null)
                {
                    q.Image = Fields[3];
                }
                else
                {
                    q.Image = "";
                }
               
                q.Like = int.Parse(Fields[4]);
                q.Dislike = int.Parse(Fields[5]);
                q.NumOfMessages = int.Parse(Fields[6]);
                q.NumOfViews = int.Parse(Fields[7]);
                q.PostedDate = DateTime.Parse(Fields[8]);
                ListOfQuestions.Add(q);
                ListOfQuestions[rowcount].ListOfAnswers = new List<Answer>();
                foreach (var ansrow in anslines)
                {
                    Answer ans = new Answer();
                    String[] ansFields = AnsParser.Split(ansrow);
                    for (int j = 0; j < ansFields.Length; j++)
                    {
                        ansFields[j] = ansFields[j].TrimStart(' ', '"');
                        ansFields[j] = ansFields[j].TrimEnd('"');
                    }
                    if (int.Parse(ansFields[0]) == q.ID)
                    {
                        ans.ID = int.Parse(ansFields[1]);
                        ans.Text = ansFields[2];
                        if (Fields[3] != null)
                        {
                            ans.Image = ansFields[3];
                        }
                        else
                        {
                            ans.Image = "";
                        }
                        ans.UpVotes = int.Parse(ansFields[4]);
                        ans.DownVotes = int.Parse(ansFields[5]);
                        ans.PostedDate = DateTime.Parse(ansFields[6]);
                        ListOfQuestions[rowcount].ListOfAnswers.Add(ans);
                    }
                }
               rowcount++;
            }
            return ListOfQuestions;
        }
    }
}
