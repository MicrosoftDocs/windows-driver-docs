---
title: Debugging Hyper-V via a Null-modem Cable Connection
description: Debugging Hyper-V via a Null-modem Cable Connection
ms.assetid: 93d78696-11fa-443b-9fbe-60d208aa91d5
---

# Debugging Hyper-V via a Null-modem Cable Connection


## <span id="ddk_opening_a_crash_dump_dbg"></span><span id="DDK_OPENING_A_CRASH_DUMP_DBG"></span>


To debug either the root partition or Windows hypervisor across a null-modem cable connection, use the following procedure.

1.  Verify that you have the proper version of Debugging Tools for Windows installed on the host computer. If you are unsure of which version to use, see [Choosing a 32-Bit or 64-Bit Debugger Package](choosing-a-32-bit-or-64-bit-debugger-package.md). To debug Hyper-V across a null-modem cable, the x64 package must be used. If a different version of the package is required for your target, use a 1394 cable to debug Hyper-V,

2.  Copy the file Kdhvcom.dll from the Debugging Tools for Windows package to the Windows\\system32 directory on the root partition of the target computer.

3.  On the target computer, use the BCDEdit tool to set the boot configuration settings to allow the debugging that you want. If you intend to debug the root partition, use the following commands:

    ```
    bcdedit /set dbgtransport kdhvcom.dll 
    bcdedit /dbgsettings serial DEBUGPORT:Port BAUDRATE:Baud
    bcdedit /debug on 
    ```

    If you intend to debug Windows hypervisor, use the following commands:

    ```
    bcdedit /hypervisorsettings serial DEBUGPORT:Port BAUDRATE:Baud
    bcdedit /set hypervisordebug on 
    bcdedit /set hypervisorlaunchtype auto 
    ```

    In these commands, *Port* represents the number of the COM port that you are using, and *Baud* represents the rate of the connection. For example, if you are using COM1 with a baud of 115,200, *Port* is **1** and *Baud* is **115200**. For details on the use of BCDEdit, see [Editing Boot Options](https://msdn.microsoft.com/library/windows/hardware/ff542279).

    If you want to enable debugging of both the root partition and Window hypervisor, use both sets of BCDEdit commands described in this step.

    After issuing these BCDEdit commands, restart the target computer.

4.  Connect the host computer and the target computer by connecting a null-modem cable between their COM ports. This is done exactly as in standard kernel debugging; for details, see [Setting Up a Null-Modem Cable Connection](setting-up-a-null-modem-cable-connection.md).

5.  Open a Command Prompt window on the host computer, and change the current directory to the root directory of the Debugging Tools for Windows installation. Run the vmdemux (virtual machine demultiplexer) tool, using the following command line:

    ```
    vmdemux -src com:port=Port,baud=Baud
    ```

    In this command, *Port* represents the number of the COM port you are using (including the "com" prefix), and *Baud* represents the rate of the connection. For example, if you are using COM1 with a baud of 115,200, *Port* is **com1** and *Baud* is **115200**. If you have already begun debugging Windows hypervisor and are restarting vmdemux, include the -channel 0 parameter as well.

    Vmdemux creates multiple named-pipe sessions across the COM connection: one channel for debugging Windows hypervisor and one channel for debugging the root partition. For each channel, vmdemux displays a connection string that can be used to connect a kernel debugger across that channel.

6.  The actual debugging session is started by using the Remote tool (Remote.exe) to launch KD. To begin debugging the root partition, use the following command:

    ```
    remote.exe /s "DbgPath\kd -k RPConnectionString -y SymPath" HyperV_ROOT 
    ```

    To begin debugging Windows hypervisor, use the following command:

    ```
    remote.exe /s "DbgPath\kd -k HVConnectionString -y SymPath" HyperV_HV 
    ```

    In these commands, *RPConnectionString* and *HVConnectionString* represent the connection strings for the root partition and Windows hypervisor, respectively, which were displayed in the output of vmdemux in the previous step. *DbgPath* represents the root directory of the Debugging Tools for Windows installation, and *SymPath* represents the symbol path. You may include other KD options as well. If you want to connect remotely to KD from another computer (using WinDbg or a second instance of KD), include the **-server** parameter followed by any permissible transport options. If you include the **-server** parameter, it must be the first parameter used.

    For example, the command to debug the root partition is similar to this:

    ```
    remote.exe /s "\debuggers\kd -k com:port=\\.\pipe\Vm1,pipe,resets=0,reconnect -y srv*c:\localstore*https://msdl.microsoft.com/download/symbols" HyperV_ROOT 
    ```

    And the command to debug Windows hypervisor is similar to this:

    ```
    remote.exe /s "c:\debuggers\kd -k com:port=\\.\pipe\Vm0,pipe,resets=0,reconnect -y srv*c:\localstore*https://msdl.microsoft.com/download/symbols" HyperV_HV 
    ```

At this point, you can debug the target normally.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Hyper-V%20via%20a%20Null-modem%20Cable%20Connection%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




