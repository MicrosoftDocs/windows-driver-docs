---
title: Debugging Hyper-V via a 1394 Cable Connection
description: Debugging Hyper-V via a 1394 Cable Connection
ms.assetid: da183635-8dc9-4092-b4c3-104304ee45f7
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging Hyper-V via a 1394 Cable Connection


## <span id="ddk_opening_a_crash_dump_dbg"></span><span id="DDK_OPENING_A_CRASH_DUMP_DBG"></span>


To debug the root partition or Windows hypervisor across a 1394 cable connection, use the following procedure.

1.  Verify that you have the proper version of Debugging Tools for Windows installed on the host computer. If you are unsure of which version to use, see [Choosing a 32-Bit or 64-Bit Debugger Package](choosing-a-32-bit-or-64-bit-debugger-package.md).

2.  On the target computer, use the BCDEdit tool to set the boot configuration settings to allow the debugging that you want. If you intend to debug the root partition, use the following commands:

    ```
    bcdedit /set dbgtransport kd1394.dll 
    bcdedit /dbgsettings 1394 CHANNEL:ChannelNumber
    bcdedit /debug on 
    ```

    If you intend to debug Windows hypervisor, use the following commands:

    ```
    bcdedit /hypervisorsettings 1394 CHANNEL:ChannelNumber
    bcdedit /set hypervisordebug on 
    bcdedit /set hypervisorlaunchtype auto 
    ```

    In these commands, *ChannelNumber* represents the number of the 1394 channel that you are using. For details on the use of BCDEdit, see [Editing Boot Options](https://msdn.microsoft.com/library/windows/hardware/ff542279).

    If you want to enable debugging of both the root partition and Window hypervisor, use both sets of BCDEdit commands described in this step, with two different 1394 channel numbers.

    After issuing these BCDEdit commands, restart the target computer.

3.  Connect the host computer and the target computer by connecting a null-modem cable between their COM ports. This is done exactly as in standard kernel debugging; for details, see [Setting Up a 1394 Cable Connection](setting-up-a-1394-cable-connection.md).

4.  The actual debugging session is started by using the Remote tool (Remote.exe) to launch KD. To begin debugging, use the following command:

    ```
    remote.exe /s "DbgPath\kd -k 1394:channel=ChannelNumber -y SymPath" RemoteID 
    ```

    In this command, *ChannelNumber* represents the 1394 channel number you used in the BCDEdit command. To debug the root partition, use the channel number you specified for it; to debug Windows hypervisor, use the channel number you specified for it. *RemoteID* represents an identifying string that is used by the Remote tool (for example, **HyperV\_ROOT** or **HyperV\_HV**). *DbgPath* represents the root directory of the Debugging Tools for Windows installation, and *SymPath* represents the symbol path. You may include other KD options as well. If you want to connect remotely to KD from another computer, (using WinDbg or a second instance of KD), include the **-server** parameter followed by any permissible transport options. If you include the **-server** parameter, it must be the first parameter used.

    For example, the command to debug the root partition is similar to this:

    ```
    remote.exe /s "\debuggers\kd -k 1394:channel=50 -y srv*c:\localstore*https://msdl.microsoft.com/download/symbols" HyperV_ROOT 
    ```

At this point, you can debug the target normally.

 

 





