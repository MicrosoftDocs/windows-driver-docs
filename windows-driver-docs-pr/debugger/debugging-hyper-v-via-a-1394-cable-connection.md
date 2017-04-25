---
title: Debugging Hyper-V via a 1394 Cable Connection
description: Debugging Hyper-V via a 1394 Cable Connection
ms.assetid: da183635-8dc9-4092-b4c3-104304ee45f7
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Hyper-V%20via%20a%201394%20Cable%20Connection%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




