---
description: The Network Monitor tool (NetMon.exe) is a Windows-based application that you can use to view traces from WPD components.
title: Using the Network Monitor Tool
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the Network Monitor Tool

The Network Monitor tool (*NetMon.exe*) is a Windows-based application that you can use to view traces from WPD components. The tool replaces *WpdMon.exe* and provides a new means of collecting and viewing WPD traces in Windows 8.

## Installing and Configuring NetMon.exe

To install and configure the Network Monitor tool, complete the following steps.

1. Download and install [*NetMon.exe*](https://go.microsoft.com/fwlink/p/?linkid=248501).
2. Download and install [the Windows Driver Kit](https://go.microsoft.com/fwlink/p/?linkid=178709).
3. Install the WPD parsers on your development machine by starting an instance of *Powershell.exe* with *Administrator* permissions and running the following sequence of commands.
   1. PowerShell -ExecutionPolicy RemoteSigned
   2. cd “\\Program Files (x86)\\Windows Kits\\8.0\\Tools\\x86\\Network Monitor Parsers\\usb”
   3. ..\\NplAutoProfile.ps1
   4. cd ..\\wpd
   5. ..\\NplAutoProfile.ps1
        **Note**  The WPD parsers are included in the Windows Driver Kit.

4. Configure the *NetMon.exe* options by using the Tools/Options dialog:
   1. In the **General** tab, select the **Use fixed width font in Frame Summary** box.
   2. In the **Color Rules** tab, select **Open** and then select \\Program Files (x86)\\Windows Kits\\8.0\\Tools\\x86\\Network Monitor Parsers\\wpd\\wpd.nmcr. Select **Open**, followed by **OK.**

After you complete these steps, *NetMon.exe* is ready to examine WPD trace files. To begin collecting traces, follow the instructions in the next section, Collecting Traces.

## Collecting Traces

To generate traces, you'll need to create a command script. Copy the following to a text file and save it with the .cmd file name extension.

```cmd
echo off
@REM ---------------------------------------------------------------------------------------
@REM UNCOMMENT THE LOGMAN COMMANDS FOR THE FOLLOWING PROVIDERS AS REQUIRED
@REM Microsoft-Windows-WPD-API                 To log API traffic
@REM Microsoft-Windows-WPD-MTPClassDriver      To log MTP command, response and datasets
@REM Microsoft-Windows-WPD-MTPUS               To log USB traffic at WpdMtpUS layer
@REM Microsoft-Windows-WPD-MTPIP               To log IP traffic at WpdMtpIP layer
@REM Microsoft-Windows-WPD-MTPBT               To log BT traffic at WpdMtpBt layer
@REM Microsoft-Windows-USB-USBPORT             To log USB core layer traffic
@REM Microsoft-Windows-USB-USBHUB              To log USB core layer traffic
@REM ---------------------------------------------------------------------------------------

@REM Start Logging

logman start  -ets WPD -p Microsoft-Windows-WPD-API            -bs 100 -nb 128 640 -o wpd_trace.etl
logman update -ets WPD -p Microsoft-Windows-WPD-MTPClassDriver -bs 100 -nb 128 640
logman update -ets WPD -p Microsoft-Windows-WPD-MTPUS          -bs 100 -nb 128 640
logman update -ets WPD -p Microsoft-Windows-WPD-MTPIP          -bs 100 -nb 128 640
logman update -ets WPD -p Microsoft-Windows-WPD-MTPBT          -bs 100 -nb 128 640
logman update -ets WPD -p Microsoft-Windows-USB-USBPORT        -bs 100 -nb 128 640
logman update -ets WPD -p Microsoft-Windows-USB-USBHUB         -bs 100 -nb 128 640
logman update -ets WPD -p Microsoft-Windows-Kernel-IoTrace 0 2
echo.
echo Please run your scenario now and
pause

@REM Stop logging
logman stop -ets WPD
```

After you create the command file, run it on your Windows 8 machine from an elevated command session.

If you used the contents of the sample command file, your traces will be stored in the file wpd\_trace.etl.

## Viewing Traces

To view your traces, launch *NetMon.exe*, select the File/Open/Capture menu and open the wpd\_trace.etl file collected above. When you open a trace file you will see that NetMon.exe displays the traces at various layers:

- WPDAPI – Displays information from WPD API level with WPD commands and responses
- WPDMTP – Displays information from MTP level with MTP commands and responses
- Transport (WPDMTPUS or WPDMTPIP or WPDMTPBT) – Shows transport level packets

The following image shows a WPDAPI request at API level. The request travels through WPDMTP in the form of MTP request(s) that reach a transport and then bubble up.

![Screenshot that shows the "Frame Summary" window with callouts for different trace layers.](images/framesummary1.png)

- The transport-level logging does not log the actual data during the data phase. Examine the WPDMTP Response message for the datasets that were sent or received during commands like **GetDeviceInfo** or **SendObjectPropList**.
- If you select a WPDMTP Response line in the **Frame Summary** window, the corresponding item expands in the **Frame Details** window.
- Select the "+"s in the **Frame Details** window to expand further and explore. If an MTP operation has a dataphase, the dataset received from the device is available under the **DataSetOfDataPhase** field of a WPDMTP Response item.

![viewing traces.](images/framedetails1.png)

- You can select to expand the items and see that the **Frame Details** window displays WPD/MTP friendly messages. The convention followed when writing the WPD parsers is that you will be able to see summary of the details at the header level. For example, in a GetServiceCapabilities call, the **DataSetOfDataPhase** field shows next to it, the number of formats in that dataset.
- You can remove the **Source** and **Destination** columns in the **Frame Summary** window to improve clarity
- When you select a field in **Frame Details** window, the corresponding value is highlighted in the **Hex Details** window.

## Filtering with NetMon.exe

The Network Monitor tool provides several filtering capabilities.

- To show only the MTP traces, enter **!wpdmtp** in the **Display Filter** window and select **Apply**.
- To filter for cases where the driver returned an error:
  - Enter **wpderror != 0** in the **Display Filter** window and select **Apply**.
- You can filter for all of the method calls for a given scenario. For example, the following filter would retrieve all of the calls to GetServiceProperties:

    WPDMTP.CorrespondingCommand.MTPOpcode == 0x9304

- Similarly, the following filter would retrieve the same method calls:

    WPDMTP.CorrespondingCommand.MTPOpcode == MTP\_OPCODE\_GETSERVICEPROPERTIES
