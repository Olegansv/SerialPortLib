using System;
using System.IO.Ports;

class serial_init
{
    static void Main(string[] args)
    {
        try
        {
            SerialPort serialPort = new SerialPort();
            string port = args[0];
            int baudRate = Convert.ToInt32(args[1]);
            serialPort.PortName = port;
            serialPort.BaudRate = baudRate;
            serialPort.Open();
            serialPort.Close();
        }
        catch
        { }
    }
}