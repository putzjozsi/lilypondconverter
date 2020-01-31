using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml;

namespace LilypondConverter
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Converting MuseScore to Lilypond");

            try
            {
                XmlDocument doc = new XmlDocument();
                doc.Load(@".\Data\kotta.mscx");

                //XmlNode node = doc.DocumentElement.SelectSingleNode("/book/title");
                // XmlNode node = doc.DocumentElement.SelectSingleNode("/book/title");
                //string attr = node.Attributes["theattributename"]?.InnerText
                foreach (XmlNode node in doc.DocumentElement.ChildNodes)
                {
                    string text = node.InnerText; //or loop through its children as well
                }

            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);                
            }


            Console.ReadKey();
        }
    }
}
