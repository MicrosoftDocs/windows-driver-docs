---
title: Setting Up QEMU Kernel-Mode Debugging Using EXDI
description: Debugging Tools for Windows supports debugging QEMU using EXDI. This topic describes how to setup QEMU kernel debugging using EXDI.
ms.date: 10/28/2024
ms.localizationpriority: medium
---

# Setting Up QEMU Kernel-Mode Debugging Using EXDI

This topic describes how to set up QEMU Kernel-Mode Debugging using EXDI with the Windows debugger.

For general information on setting up configuring and troubleshooting EXDI connections, see [Configuring the EXDI Debugger Transport](configuring-the-exdi-debugger-transport.md).

Using QEMU, the virtualization and machine emulation software, it is possible to connect to other operating systems serving as the host, such as Linux. QEMU itself can run on numerous architectures, such as x64 and Arm64. The ExdiGdb debugging server also supports other processors, for example it is possible to use WinDbg to debug QEMU running on x64, emulating Arm64. Using EXDI also allows the VM to be HW debugged early in the boot process, even before the OS has loaded. 

>[!NOTE]
> EXDI is an advanced, specialized form of debugging for specific environments. Using a standard KDNET connection is easier to configure, and is recommended.  To set up network debugging automatically, see **[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)**.

## EXDI COM Server

EXDI is an interface that allows extending WinDbg by adding support for hardware debuggers (e.g. JTAG-based, or GdbServer based). The diagram below illustrates the role of EXDI-GdbServer.

:::image type="content" source="images/exdi-server-dbgeng-interface-diagram.png" alt-text="Stack diagram showing the role of EXDI-GdbServer with WinDbg-DbgEng on top, an EXDI interface, and an EXDI COM server communicating with a GDB server.":::

>[!IMPORTANT]
> Because EXDI does not make use of the KDNET protocol, the connected debugger has significantly less information about what is running on the PC and many commands will work differently or may not work at all. Access to private symbols for the code being debugged can help the debugger better understand the target systems code execution. For more information, see [Public and Private Symbols](public-and-private-symbols.md).

## Setup a debugger connection to a Windows Image on QEMU
These steps describe how to attach to a Windows x64 Virtual Machine exposing a GDB server to a Windbg client (which uses the EXDI COM server), also running on Windows. A GdbServer RSP session between the WinDbg ExdiGdbSrv.dll (GDB server client) and QEMU GDB server is used.
  
1. Download and install QEMU on Windows.
1. Configure a target QEMU virtual Windows image to launch with the required network and BIOS/UEFI settings for debugging.
1. Start the QEMU environment, using a launch script.
1. Start the GdbServer on QEMU.
1. Check network connectivity and locate and record the target image IP address. (HOST IP default address of LocalHost, and port of 1234).
1. Download and install the Windows debugging tools on the host system.
1. Launch WinDbg using the command line or UI to connect to the EXDI server.
1. Use WinDbg to debug the target QEMU Windows image.

## QEMU open-source machine emulator

QEMU is a generic and open-source machine emulator and virtualizer that causes dynamic translation. When QEMU is used as a machine emulator - it can run OS’s and programs made for one processor (such as an Arm64) on a different machine (an x64 PC). It can also run/host virtual machines images for different OS's (Windows/Linux/Mac).

QEMU can operate with other hypervisors like KVM to use CPU extensions (HVM) for virtualization. When QEMU is used as a virtualizer, QEMU achieves near native performances by executing the guest code directly on the host CPU. QEMU can take advantage of OS hypervisor features to offload CPU and MMU emulation to real hardware.

### Download and Install QEMU

In this walk through, QEMU for Windows x64 will be installed on an x64 PC where the Windows debugger will also run on.

Download QEMU from the QEMU download page: https://www.qemu.org/download/

Refer to the QEMU documentation for information on installing QEMU: https://www.qemu.org/documentation/

### Configure a Target Virtual Disk

Locate or create a virtual disk image that has the software that you wish to debug.

In this example, a Windows x64 VHDX virtual machine disk image will be used. To learn more about Windows virtual machine images, see [Create Virtual Machine with Hyper-V on Windows 10](/virtualization/hyper-v-on-windows/quick-start/create-virtual-machine).

### Inject the VirtIO drivers into the Windows Image

To allow network functionality and reasonable storage device performance, either inject or install the VirtIO drivers into the Windows virtual machine disk image. The VirtIO drivers are available here: https://github.com/virtio-win/kvm-guest-drivers-windows

VirtIO is a standardized interface which allows virtual machines access to abstracted hardware, such as block devices, network adapters and consoles. VirtIO serves as an abstraction layer to hardware devices in a virtualized environment like QEMU. 

To inject the VirtIO driver into the Windows image follow the steps below:

1.	Extract the VirtIo drivers in a folder, for example `C:\VirtIo_Drivers`.
2.	Mount the VHDX containing the Windows x64 Virtual machine by double clicking on the VHDX in File Explorer (you can use also diskpart). Windows will mount the VHDX using a specific letter, for example “L:”
3.	Inject the driver in the mounted image using Dism: `dism /image:L: /Add-Driver /driver:C:\VirtIo_Drivers` For more information about DISM, see [DISM Overview](/windows-hardware/manufacture/desktop/what-is-dism).
4.	When the process completes, you can unmount the image and proceed to convert the VHDX to QEMU.

### Convert VHDX to QEMU

This step is not required, but it is recommended, as better performance is achieved when using a native QEMU QCOW image instead of a VHDX.

Use the following qemu-img.exe command to convert the vhdx. This utility is located where you installed QEMU, for example `C:\Program Files\qemu`.

```Console
C:\Program Files\qemu> qemu-img convert -c -p -O qcow2 MyVHDXFile.vhdx MyQEMUFile.qcow2 
```

### Download UEFI Firmware

For the best results, download or compile the UEFI firmware file (OVMF.fd). The firmware is needed because otherwise by default QEMU emulates older BIOS systems.

One source for UEFI Firmware is the Open Clear Linux project:
https://clearlinux.org/

The example UEFI `OVMF.fd` file is available here:
https://github.com/clearlinux/common/tree/master/OVMF.fd

Extract the content of the downloaded file in `C:\Program Files\qemu\Firmware`.  

For platforms other than Intel AMD64 you should compile the firmware from the EDK2. For more information, see https://github.com/tianocore/tianocore.github.io/wiki/How-to-build-OVMF.


### Configure QEMU Launch Script

Create your configuration file in QEMU. For example, create a `StartQEMUx64Windows.bat` file under the QEMU root directory. See the example file below.

#### Use the QEMU Launch Script to start QEMU

Execute the QEMU launch script to start QEMU.

```bat
c:\Program Files\qemu\StartQEMUx64Windows.bat
```

If a firewall defender prompt appears, grant the app all rights to all types of networks to enable Windbg through the Windows firewall for the host debugger machine.

:::image type="content" source="images/exdi-windows-defender-firewall-dialog.png" alt-text="Windows Defender Firewall dialog box with all three options checked.":::

Once the Windows Virtual Machine is launched in the QEMU environment the QEMU UI will appear.

:::image type="content" source="images/exdi-windows-qemu-view-menu.png" alt-text="Screenshot of QEMU displaying view menu options.":::

Use CTRL+ALT+ a number key combination to go in the QEMU monitor console. This monitor is also available using *View->compatmonitor*.

Type `gdbserver` to launch the front end GDB server on QEMU.

QEMU should display `Waiting for gdb connection on device ‘tcp::1234’`

Return to the main window using the CTRL+ALT+1 keys combination.

Tip: The GDB console window supports the `system_reset` command to quickly restart the emulation. Type `help` for a list of GDB console commands.

### Sample of QEMU x64 Windows VM launching script

Here is an example QEMU configuration script that can be used for AMD64 Virtual Machines. Replace the links that point to the DISK and CDROM files to the locations on your PC. 

```bat
    REM
    REM  This script is used to run a Windows x64 VM on QEMU that is hosted by a Windows x64 host system
    REM  The Host system is a PC with Intel(R) Xeon(R) CPU.
    REM
    set EXECUTABLE=qemu-system-x86_64
    set MACHINE=-m 6G -smp 4

    REM No acceleration
    REM generic cpu emulation.
    REM to find out which CPU types are supported by the QEMU version on your system, then run:
    REM	 qemu-system-x86_64.exe -cpu help
    REM the see if your host system CPU is listed
    REM

    set CPU=-machine q35 

    REM Enables x64 UEFI-BIOS that will be used by QEMU :
    set BIOS=-bios "C:\Program Files\qemu\Firmware\OVMF.fd"

    REM  Use regular GFX simulation
    set GFX=-device ramfb -device VGA 
    set USB_CTRL=-device usb-ehci,id=usbctrl
    set KEYB_MOUSE=-device usb-kbd -device usb-tablet

    REM # The following line enable the full-speed HD controller (requires separate driver)
    REM # Following line uses the AHCI controller for the Virtual Hard Disk:
    set DRIVE0=-device ahci,id=ahci -device ide-hd,drive=disk,bus=ahci.0

    REM
    REM This will set the Windows VM x64 disk image that will be launched by QEMU
    REM The disk image is in the qcow2 format accepted by QEMU.
    REM You get the .qcow2 image, once you get the VHDX Windows VM x64 image 
    REM and apply the script to inject the virtio x64 drivers and then run the 
    REM the QEMU tool to convert the .VHDX image to .qcow2 format
    REM 	i.e. 
    REM	qemu-img convert -c -p -O qcow2 Windows_VM_VHDX_with_injected_drivers_file.vhdx file.qcow2
    REM file : points to the specified qcow2 image path.
    REM
    set DISK0=-drive id=disk,file="C:\Program Files\qemu\MyQEMUFile.qcow2",if=none

    REM
    REM for kdnet on, then best option:
    REM   NETWORK0="-netdev user,id=net0,hostfwd=tcp::53389-:3389,hostfwd=tcp::50001-:50001 -device virtio-net,netdev=net0,disable-legacy=on"
    REM
    REM Create a mapping for the RDP service from port 3389 to 3589.
    REM
    set NETHOST=-netdev user,id=net0,hostfwd=tcp::3589-:3389
    set NETGUEST=-device e1000,netdev=net0

    REM # The following line should enable the Daemon (instead of interactive)
    set DAEMON=-daemonize"
    %EXECUTABLE% %MACHINE% %CPU% %BIOS% %GFX% %USB_CTRL% %DRIVE0% %DISK0% %NETHOST% %NETGUEST%
```

## Network connectivity

### Local Host

If the GDB server started properly, then you will see the port number where the GDB server will be listening, and you will need to use this port to setup the host debugger `IP:Port` pair.

If your Host debugger is located at the same machine that host the QEMU guest, then the Localhost identifier will be used in the in the IP:Port pair. In this example, with the server and host debugger on the same PC, `LocalHost:1234` will be used.  

### Remote Host

If working on a remote PC, locate the Windows IP address (if the debugger host session won't be located at the same Windows machine as QEMU VM).

The target QEMU IP `<address>`:`<port number>` will be configured in the EXDI UI.

The following commands can be issued on the QEMU console (compatmonitor0) to display information about the network and connection status.

```console
info network
info usernet
```

For additional information on QEMU networking, see https://wiki.qemu.org/Documentation/Networking

## Download and install the Windows debugging tools on the host system

Install the Windows Debugging Tools on the host system. For information on downloading and installing the debugger tools, see [Debugging Tools for Windows](debugger-download-tools.md).

## Launch WinDbg on the host system

In the scenario described here, set the following options in the EXDI UI to connect. 

Target type - *QEMU*

Target architecture - *x64*

Target OS - *Windows*

Image scanning heuristic size - *0xFFE - NT*

Gdb server and port - *LocalHost:1234*

Break on connections - *yes*

:::image type="content" source="images/windbgx-exdi-server-config-ui.png" alt-text="Windbg EXDI kernel connection UI, with connection options shown, including IP and port address.":::

Although the use of the EXDI UI is recommended, it is also possible to launch WinDbg using the command line option similar to what is shown here.

```dbgcmd
c:\Debuggers> windbg.exe -v -kx exdi:CLSID={29f9906e-9dbe-4d4b-b0fb-6acf7fb6d014},Kd=Guess,Inproc=ExdiGdbSrv.dll,DataBreaks=Exdi
```
When using the command line, the IP address and port are configured using the  exdiConfigData.xml file. For more information, see [EXDI XML Configuration files](exdi-xml-configuration-files.md).

To display additional output, the **-v:** verbose session can be used. For general information about the WinDbg options, see [WinDbg Command-Line Options](windbg-command-line-options.md).

The debugger should launch and connect to the QEMU GdbServer.

:::image type="content" source="images/exdi-windbg-debugger-session.png" alt-text="Main WinDbg session displaying EXDI CLSID in the window title.":::

The debugger will show the successful EXDI transport initialization.

```dbgcmd
EXDI: DbgCoInitialize returned 0x00000001
EXDI: CoCreateInstance() returned 0x00000000
EXDI: QueryInterface(IExdiServer3) returned 0x00000000
Target command response: QEMU
exdiCmd: The function: 'ExdiDbgType' was completed.
EXDI: Server::GetTargetInfo() returned 0x00000000
EXDI: Server::SetKeepaliveInterface() returned 0x00000000
EXDI: Server::GetNbCodeBpAvail() returned 0x00000000
EXDI: ExdiNotifyRunChange::Initialize() returned 0x00000000
EXDI: LiveKernelTargetInfo::Initialize() returned 0x00000000
EXDI: Target initialization succeeded
```

The EXDIGdbServer console packets window can also display information about the status of the EXDI connection, if *"*Show communication packet log* under Advanced options is set to on. For more information, refer to the troubleshooting information in [Configuring the EXDI Debugger Transport](configuring-the-exdi-debugger-transport.md#troubleshooting).

### Use WinDbg to debug the target QEMU Windows image

The dbgeng.dll uses a heuristic algorithm to find the location of the NT base load address at the time that the break command occurred.  If private symbols are not available, this process will fail.

This means that under many connection sequences, the break will not function as expected. if you manually break into the code, it will be a random location that Windows happened to be executing at that moment. As symbols for the target code may not be available, it can be difficult to set breakpoints using symbols.

### Available debugger memory access commands

Commands such as the following that access memory directly will work.

[k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md)

[r (Registers)](../debuggercmds/r--registers-.md)

[d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)](../debuggercmds/d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md)

[u (Unassemble)](../debuggercmds/u--unassemble-.md)

And you can step through code.

[p (Step)](../debuggercmds/p--step-.md)

There are also commands that can be used to attempt to locate code that you wish to debug.

[s (Search Memory)](../debuggercmds/s--search-memory-.md)

[.imgscan (Find Image Headers)](../debuggercmds/-imgscan--find-image-headers-.md)

Imgscan can be helpful with EDXI debugging, as unlike traditional KDNET based kernel debugging, setting breakpoints based on symbols may not be available. Locating a desired target image, can facilitate using its location to set a memory access breakpoint.

### .exdicmd (EXDI Command)

The .exdicmd sends an EXDI command to the target system using the active EXDI debugging connection. For more information, see [.exdicmd (EXDI Command)](../debuggercmds/-exdicmd--exdi-command-.md).

## Troubleshooting

Refer to the troubleshooting information in [Configuring the EXDI Debugger Transport](configuring-the-exdi-debugger-transport.md#troubleshooting).

## See also

[Configuring the EXDI Debugger Transport](configuring-the-exdi-debugger-transport.md)

[EXDI XML Configuration files](exdi-xml-configuration-files.md)

[.exdicmd (EXDI Command)](../debuggercmds/-exdicmd--exdi-command-.md)

[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)

[Setting Up KDNET Network Kernel Debugging Manually](setting-up-a-network-debugging-connection.md)
