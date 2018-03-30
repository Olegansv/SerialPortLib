﻿using System;
using System.IO.Ports;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            using (SerialPort serialPort = new SerialPort(args[0], Convert.ToInt32(args[1])))
            {
                serialPort.Open();
                serialPort.Close();
            }
        }
        catch { }
    }
}
