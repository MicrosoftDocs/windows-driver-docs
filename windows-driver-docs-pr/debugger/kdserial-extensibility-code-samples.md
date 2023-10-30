---
title: KDNET Serial, and KDSerial extensibility code samples
description: Debugging Tools for Windows supports extending the KDNET serial transport.
ms.date: 04/14/2022
---

# Example KDSerial extensibility code samples

Debugging Tools for Windows supports extending the KDNET serial transport. KDNET transport extensibility modules are developed by hardware vendors to add kernel debugging support to specific hardware that is not already supported.

In general, serial connections for debugging are slower, so using the KDNET over an ethernet card is preferred option, when at all possible.

## Example KDSerial extensibility code samples

The following three code samples are available in the WDK install directory and show the use of the KDNET Serial and KDSerial transport extensions.

### KDNET Serial 16550 Sample

The KDNET serial interface, shows the use of 16550 serial interface hardware. It is located in the this directory.

`C:\Program Files (x86)\Windows Kits\10\Debuggers\ddk\samples\kdnet\serial\16550`

When testing the KDNET Serial 16550 sample code, the serial cable should be wired as a NULL-MODEM RS232 cable, where the Tx-Rx lines are crossed.


### KDNET Serial siig Sample

The siig sample implements KDNET over serial with RS-232 hardware handshaking. It is located in the this directory.

`C:\Program Files (x86)\Windows Kits\10\Debuggers\ddk\samples\kdnet\serial\siig`

When testing the KDNET serial siig code sample, the serial cable should be wired as a straight through RS-232 cable.


### KDSerial Sample

This shows the use of the older KDSerial transport. The KDNET transport over serial is preferred. 

`C:\Program Files (x86)\Windows Kits\10\Debuggers\ddk\samples\kdserial`

When testing the KDSerial code sample, the serial cable should be wired as a NULL-MODEM RS232 cable, where the Tx-Rx lines are crossed.


## Steps to deploy test serial kernel debug transport

1) Load and build project (outputs kdserial.dll)

2) Rename kdserial.dll to kdcom.dll

3) Copy kdcom.dll to `C:\windows\system32\kdcom.dll` on target machine (Advised
    to create a backup of original kdcom.dll before overwriting it)

4) Run `bcdedit /dbgsettings serial debugport:<port> baudrate:<rate>` on target

5) Run `bcdedit /debug on` on target

6) Run `bcdedit /bootdebug on` on target

7) Run `bcdedit /testsigning yes` on target

8) Reboot target & connect to boot debugger. This step is required for the new kdcom.dll to be loaded without a valid Microsoft signature. If the boot debugger is not enabled & connected when kdcom.dll is being loaded, winload will fail to load it.

NOTE: the custom kdcom.dll will not be used for the boot debugger transport

9) Continue through winload & connect to the kernel debugger via the custom kdcom.dll transport.

## See also

[How to develop KDNET extensibility modules](how-to-develop-kdnet-extensibility-modules.md) 

[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)

[Setting Up KDNET Network Kernel Debugging Manually](setting-up-a-network-debugging-connection.md)

[Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)
