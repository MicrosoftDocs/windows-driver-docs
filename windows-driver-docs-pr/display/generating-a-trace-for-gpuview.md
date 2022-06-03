---
title: Generating a Trace for GPUView
description: "Before you can use GPUView to view video and kernel events, you must create an event trace log (.etl) file that contains the events."
ms.date: 05/10/2022
---

# Generating a Trace for GPUView

Before you can use GPUView to view video and kernel events, you must create an event trace log (.etl) file that contains the events. The GPUView install package places two custom-designed script files (Log.cmd and Circularlog.cmd) in the same location as GPUView. You can use these script files to start and stop the event logging process and to generate the merged ETL file that GPUView reads.

## Using Log.cmd

To generate an ETL file, you must run Log.cmd from an administrator-level command prompt. To start an administrator-level command prompt on Windows Vista, click the Start button, search for cmd, right-click the product of the search (**cmd**), and select **Run as administrator**. 

To start event trace logging, run Log.cmd. To stop event trace logging, run the same Log.cmd. Running Log.cmd produces a Merged.etl file that GPUView can read. 

To load this ETL file into GPUView, run GPUView from the command prompt (for example, GPUView Merged.etl). Alternatively, you can associate GPUView with ETL files and then double-click the Merged.etl file. 

Note that the buffers that are used to store event messages in the ETL file are circular buffers. Storing event messages in circular buffers limits the amount of time that you can spend between the start and the end of logging to less than a minute. You should set up test scenarios so that you can turn on logging immediately before an unusual condition and turn off logging again before a minute has elapsed. 

You should read through the Log.cmd file that performs the work on behalf of the other scripts or read through the information that is provided with WPT regarding the creation of ETL files. The basic providers for multimedia events are shown in the Log.cmd file. You can activate these events through the command-line parameters of Log.cmd. 

You can use the following command-line parameters with Log.cmd to log your required type and number of events.

| Command | Description | Meaning                                     |
|---------|-------------|---------------------------------------------|
| Log m   | Minimum     | Log only the minimum basic events           |
| Log l   | Light       | Log only a few more than the minimum events |
| Log     | Normal      | Log the most interesting events             |
| Log v   | Verbose     | Log everything that GPUView is aware of     |

## Using Circularlog.cmd

If you do not know exactly when the issue that you are trying to capture is going to occur, you can enable logging in the background and either flush or stop logging just after the issue that you want to debug occurs. To do this, you can use the custom script Circularlog.cmd. 

The Circularlog.cmd script is similar to Log.cmd in that it has four different logging levels, but different in that it takes advantage of the circular logging functionality provided by the Windows event log infrastructure. 

We recommend that the user read through the Circularlog.cmd file to better understand its function. 

You can use the following command-line parameters with Circularlog.cmd to log your required type and number of events. 

| Command           | Description | Meaning                                                                    |
|-------------------|-------------|----------------------------------------------------------------------------|
| Circularlog m     | Minimum     | Log only the minimum basic events                                          |
| Circularlog l     | Light       | Log only a few more than the minimum events                                |
| Circularlog       | Normal      | Log the most interesting events                                            |
| Circularlog v     | Verbose     | Log everything that GPUView is aware of                                    |
| Circularlog flush | Flush       | Write the information in the circular buffers to files and merge the files |
| Circularlog stop  | Stop        | Perform a flush and then stop logging                                      |

