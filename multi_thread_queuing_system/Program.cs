using System;
using System.Threading;
using System.Collections;

namespace C_sharp
{
    class Program
    {
        static Queue input = new Queue();
        static Queue output = new Queue();
        private static Mutex mut = new Mutex();

        public static void get_input(){
            while(true){
                int val = Convert.ToInt32(Console.ReadLine());
                input.Enqueue(val);
            }
        }

        public static void print_output(){
            while(true){
                if(output.Count>0){
                    int val = Int32.Parse(output.Dequeue().ToString());
                    Console.WriteLine("***" + val + "***");
                }
            }
        }

        public static void update(object id)
        {
            int? val = null;
            Console.WriteLine("thread ID: " + id);
            while(true){
                mut.WaitOne();
                if (input.Count>0){
                    val = Int32.Parse(input.Dequeue().ToString());
                }
                else{
                    val = null;
                }
                mut.ReleaseMutex();

                if(!String.IsNullOrEmpty(val.ToString())){
                    Console.WriteLine("thread ID: " + id + " is processing " + val.ToString() + " -- START");
                    output.Enqueue(val + 1);
                    Thread.Sleep(500);
                    Console.WriteLine("thread ID: " + id + " is processing " + val.ToString() + " -- STOP");
                }
                Thread.Sleep(500);
            }
        }
        
        static void Main(string[] args)
        {
            int max_no_of_thread = 5;
            input.Enqueue(1);
            input.Enqueue(2);
            input.Enqueue(3);
            input.Enqueue(4);
            input.Enqueue(5);
            input.Enqueue(6);
            input.Enqueue(7);
            input.Enqueue(8);
            input.Enqueue(9);
            input.Enqueue(0);
            
            Thread thr0 = new Thread(get_input);
            thr0.Start();
            Thread thr1 = new Thread(print_output);
            thr1.Start();

            for(int i=0;i<max_no_of_thread;i++){
                Thread thr2 = new Thread(update);
                thr2.Start(i.ToString());
            }

            input.Enqueue(11);
            input.Enqueue(12);
            input.Enqueue(13);
            input.Enqueue(14);
            input.Enqueue(15);
        }
    }
}