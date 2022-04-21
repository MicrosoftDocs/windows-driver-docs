---
title: Develop KDNET transport extensibility modules
description: This topic describes how the KDNET transport can be extended to run on any hardware through the use of a separate hardware driver extensibility module dll.  
ms.date: 04/14/2022
---

# Develop KDNET transport extensibility modules

This topic describes how the KDNET transport can be extended to run on any hardware through the use of a separate hardware driver extensibility module dll.  KDNET transport extensibility modules are developed by network card vendors to add kernel debugging support to specific network cards.

## KDNET Overview

KDNET is a kernel debug transport that enables kernel debugging of windows over a network.  Initially it was used to support kernel debugging with Ethernet NICs.  It is designed so that the hardware support layer is built into a separate module from the network packet processing and kernel interface layer.  This hardware driver support layer is called a KDNET extensibility module.

KDNET is the only transport that can be extended to run on any hardware through the use of a separate hardware driver extensibility module dll.  It is the goal to support all debugging of Windows through KDNET and KDNET extensibility modules.  All other kernel transport DLLs (kdcom.dll, kd1394.dll, kdusb.dll, etc.) will eventually be deprecated and removed from Windows.

There are two types of interfaces that KDNET uses to communicate with KDNET extensibility modules.  One is a packet based interface that is used for NICs, USB, and wireless hardware, and the other is a byte based interface that is used to support KDNET over serial hardware.

KDNET extensibility modules must follow very stringent requirements in order to operate correctly.  Because they are used for kernel debugging they will be called and executed when the system is holding off further execution of code.  Generally, all of the processors in the system are locked up spinning in an IPI except for the processor that is communicating with the debugger application running on the host machine through the kernel debug transport.  That processor is typically running with interrupts completely disabled, and is essentially spinning on the debug transport hardware waiting for commands to come from the debugger.

KDNET extensibility modules have exactly one explicit export – KdInitializeLibrary.  They also have no explicit imports.  KDNET extensibility modules are passed a pointer to a structure with a list of the routines they are allowed to call by KDNET when it calls KdInitializeLibrary. No other routines can be called.  Period.  KDNET extensiblity modules that have any imports are incorrectly designed, and will not be supported.

If you dump the imports and exports of a KDNET extensiblity modules using link /dump /exports and link /dump /imports, you will see they have only one export (KdInitializeLibrary), and no imports. KDNET extensibility modules report their additional exports to KDNET by filling in function pointers in an export functions structure to which KDNET passes a pointer when KdInitializeLibrary is called.  KDNET then uses the function pointers in that structure to call into the extensibility module and effect data transfers using the hardware supported by the module.  KDNET determines whether the module is a packet based or byte based module by looking at which specific functions the module fills in in the export function table in the structure.  Some of those functions are for supporting packet based hardware, and others are for serial based hardware.  Some of the functions in the table are used by both serial and packet based hardware (KdInitializeController, KdShutdownController, KdGetHardwareContextSize).

KDNET extensibility modules should be written as single threaded code.  They should not perform any synchronization.  All kernel debug transports depend on the Windows kernel to do the proper synchronization when the debugger is entered.  The kernel has a debugger lock that it takes when it enters the kernel debugger, and it also locks up the other processors in the system in an IPI when the debugger is entered.  Those processors will be released, only when the kernel debugger running on the host tells the target machine to allow execution to continue.  Because the kernel does this synchronization, the KDNET extensibility modules must absolutely not use any spinlocks, mutexes, gates, or any other Windows synchronization mechanism in their code.  They should be written to directly program their respective hardware to send and receive packets and or bytes.

KDNET extensibility module code should be made as absolutely simple as possible.  This will help ensure that it is as bug free as possible, since debugging KDNET extensibility module code live on a machine is currently not possible without the use of a hardware debugger.  You cannot use the kernel debugger to debug the kernel debug transport code.  Attempting to do so will cause the machine to reboot due to a blown kernel stack (which typically ends with a double fault and reboot), or deadlock, or will cause the transport to be reentered, which in most cases will cause the transport to not work correctly.

Your kernel debug transport module must follow one of two naming conventions for KDNET extensibility modues.  If your module is for supporting PCI based, hardware, then it must be named kd_YY_XXXX.dll where XXXX is the PCI vendor ID of your hardware in hex, and YY is the PCI class for your hardware.  There are several KDNET extensibility modules that ship in the box in windows that support PCI based hardware.  For example, Intel’s kd_02_8086.dll, Broadcom’s kd_02_14e4.dll, and Realtek’s kd_02_10ec.dll.  You can look up registered PCI vendor IDs at https://www.pcisig.com/membership/member-companies  All of the PCI based KDNET extensibility modules use the vendor VID of the hardware they support in hex as the last 4 characters in the name of their module.  The class code for most of the in box modules is 02, because they are network class devices, and therefore have a PCI class of 0x02 in their PCI config space.  Winload.exe builds the name of PCI based KDNET extensibility modules by reading the PCI device class and the PCI VID of the selected debug device from its PCI configuration space, and tries to load a module with those identifiers in the name.  If your device has a PCI class code that is not the network 0x02 class, then you must use the correct PCI class code in hexadecimal for your device, in the name of your KDNET extensibility module.  Otherwise, your module will not be loaded correctly by winload.  The `_02_` in each of those names is the PCI class code for network class devices in hex.  This code is also found and read from the PCI configuration space of the debug device.

If you have a device that has a DBG2 table entry, and is not a PCI based device, then the naming convention for your module is different.  The naming convention for DBG2 table debug devices is kd_XXXX_YYYY.dll where XXXX is the hex DBG2 table PortType, and YYYY is the hex DBG2 table PortSubtype from the DBG2 table entry.  Kd_8003_5143.dll is an inbox DLL for supporting a net (0x8003) PortType with a subtype of 0x5143.  In this case 5143 is the Qualcomm PCI vid, since this is for supporting KDNET on Qualcomm USB controllers, and for Net DBG2 table entries the PortSubtype is defined to be the PCI VID for the vendor of the hardware.  Note that you can support serial, USB and other DBG2 table devices using this naming convention.  The following are the currently supported PortType values in hex:  8000 for serial devices, 8001 for 1394 devices, 8002 for USB devices, 8003 for NET devices.  Note that the subtypes for serial and USB devices must be reserved with Microsoft.  Microsoft maintains a list of the allocated serial and USB subtypes.  Please send mail to kdnet@microsoft.com to reserve a serial or USB subtype, if the existing supported types will not work with your hardware.

## KDNET Extensibility Imports

The following is the list of routines that you can call from a KDNET extensibility module.  Note that all of these routines are passed to the KdInitializeLibrary routine, and the kdnetextensibility.h header will remap normal calls to these routines to go through the import table.  Your code must call these through the import table, so that your module has no imports.  You may not call any other routines that are exported by the kernel, the HAL, or any other kernel module.  You may only call these routines.  This set of routines has proved sufficient to develop all of the in box KDNET extensibility modules, and should suffice for normal scenarios.  If you require additional routines that are exported by the kernel, but are not in this list, please send mail to kdnet@microsoft.com explaining your scenario, and which additional routines you require and why.  Note that this list will only be added to, on major Windows release cycles if at all.  Note that most of these routines correspond directly to Windows kernel APIs that are supported by either the kernel or the HAL.   One or two are custom KDNET only routines.

It is critical that you include kdnetextensibility.h properly in your headers so that the correct remapping of routines through the import table can occur.  If this is not done, your module will have imports, and will not be supported.

The following routines should be used for reading and writing to memory mapped device memory.  These have the same calling convention and are mapped to their corresponding kernel routines: READ_REGISTER_UCHAR, READ_REGISTER_USHORT, READ_REGISTER_ULONG, WRITE_REGISTER_UCHAR, WRITE_REGISTER_USHORT, WRITE_REGISTER_ULONG and on 64 bit platforms only READ_REGISTER_ULONG64 and WRITE_REGISTER_ULONG64.   All device memory access should be done through these routines, as they ensure that reads and writes are not reordered by the processor.  Note that the msdn.microsoft.com documents Windows CE Compact 2013 routines that correspond in calling convention to these routines.  Unfortunately it appears the NT routines are not documented, but the calling convention is the same.

The following routines should be used for reading and writing to device IO ports.  These have the same calling convention and are mapped to their corresponding kernel routines: READ_PORT_UCHAR, READ_PORT_USHORT, READ_PORT_ULONG, WRITE_PORT_UCHAR, WRITE_PORT_USHORT and WRITE_PORT_ULONG.   All device IO port access should be done through these routines.  Note that the msdn.microsoft.com documents Windows CE Compact 2013 routines that correspond in calling convention to these routines.

The following additional routines can be called, and should be called normally with the specified parameters.  Note that doing so, while properly including the kdnetextensibility.h header, will remap the function calls through the KDNET extensibility import table, resulting in no explicit imports in your module as is required for KDNET extensibility modules.

```cpp
PHYSICAL_ADDRESS

KdGetPhysicalAddress (

    __in PVOID Va

    );
 

VOID

KeStallExecutionProcessor (

    __in ULONG Microseconds

    );


ULONG

KdGetPciDataByOffset (

    __in ULONG BusNumber,

    __in ULONG SlotNumber,

    __out_bcount(Length) PVOID Buffer,

    __in ULONG Offset,

    __in ULONG Length

    );
 

ULONG

KdSetPciDataByOffset (

    __in ULONG BusNumber,

    __in ULONG SlotNumber,

    __in_bcount(Length) PVOID Buffer,

    __in ULONG Offset,

    __in ULONG Length

    );

 
VOID

KdSetDebuggerNotPresent (

    __in BOOLEAN NotPresent

    );
 

VOID

PoSetHiberRange (

    _In_opt_ PVOID MemoryMap,

    _In_ ULONG     Flags,

    _In_ PVOID     Address,

    _In_ ULONG_PTR Length,

    _In_ ULONG     Tag

    );

 

VOID

KeBugCheckEx (

    __in ULONG BugCheckCode,

    __in ULONG_PTR BugCheckParameter1,

    __in ULONG_PTR BugCheckParameter2,

    __in ULONG_PTR BugCheckParameter3,

    __in ULONG_PTR BugCheckParameter4

    );


PVOID

KdMapPhysicalMemory64 (

    _In_ PHYSICAL_ADDRESS PhysicalAddress,

    _In_ ULONG NumberPages,

    _In_ BOOLEAN FlushCurrentTLB

    );
 

VOID

KdUnmapVirtualAddress (

    _In_ PVOID VirtualAddress,

    _In_ ULONG NumberPages,

    _In_ BOOLEAN FlushCurrentTLB

    );
 

ULONG64

KdReadCycleCounter (

    __out_opt PULONG64 Frequency

    );
```

Note that the PoSetHiberRange function should only be called from the KdSetHibernateRange routine.  Also, most KDNET extensibility modules should not need to call KeBugCheckEx, KdMapPhysicalMemory64 and KdUnmapVirtualAddress.  On the other hand essentially all KDNET extensibility modules will need to call KdGetPhysicalAddress for getting physical memory addresses required to program device DMA engines, and many will need to call KeStallExecutionProcessor, KdGetPciDataByOffset and KdSetPciDataByOffset.  The last two routines are for accessing device PCI config space.

## KDNET Extensibility Exports

The following is a brief description of each of the KDNET extensibility routines.  You must implement all of the routines required for either a packet based KDNET extensiblity module, or a serial based KDNET extensibility module.  The following are the packet KDNET extensiblity module exports.

### KdInitializeLibrary 
 
```cpp
NTSTATUS

KdInitializeLibrary (

    __in PKDNET_EXTENSIBILITY_IMPORTS ImportTable,

    __in_opt PCHAR LoaderOptions,

    __inout PDEBUG_DEVICE_DESCRIPTOR Device

    )

/*++

Routine Description:

    This routine validates that the ImportTable is a supported version.  Makes
    a copy of the ImportTable in its own global memory, and writes pointers to
    functions that it exports into the Exports pointer also located in that
    table.

    This routine also writes the size in bytes of the Memory it needs into
    the Length field of the Memory structure contained in the debug device
    descriptor passed to this routine.

    When kenrel debugging is enabled, this routine will be called twice during
    boot.  The first time by winload to determine how much memory to allocate
    for KDNET and its extensibility module, and the second time by KDNET when
    the kernel first initializes the kernel debugging subsystem.

Arguments:

    ImportTable - Supplies a pointer to the KDNET_EXTENSIBILITY_IMPORT
        structure.

    LoaderOptions - Supplies a pointer to the LoaderOptions passed to the
        kernel.  This allows settings to be passed to the KDNET extensibility
        module using the loadoptions BCD setting.

    Device - Supplies a pointer to the debug device descriptor.

Return Value:

    STATUS_INVALID_PARAMETER if the version of the import or export table is
        incorrect.

    STATUS_SUCCESS if initialization succeeds.
--*/
```

This routine is called to pass the import and export routines between KDNET and this KDNET extensibility module.  This routine should validate that the version of both the import and export tables is expected and supported, and fail if not.  It should make a copy of the import table in its own global memory.  It should write the routines it exports into the structure pointed to by the Exports field of the import table.  It must also set the Length field of the Memory structure that is part of the debug device descriptor pointer passed to this routine, with the number of bytes of memory that it requires to support the hardware device.

Note that device will be populated with the hardware selected for the debugger.  This routine should customize the amount of memory required based on the device, if needed.  For example, extensibility modules that support both 1Gig and 10Gig hardware, can increase the memory size they request for 10Gig devices.  They can determine which device is being used by examining the DeviceID field of the debug device descriptor.

Note that this routine will be called both by winload, and by KDNET during the KdInitSystem call.  Note that this is the ONLY routine that is exported by KDNET extensibility modules.  It is the only routine placed in a .def file.  KDNET extensibility modules have exactly one explicit export – this routine – and no imports.

### KdSetHibernateRange

```cpp
VOID

KdSetHibernateRange (

    VOID

    )

/*++
Routine Description:

    This routine is called to mark the code in the KDNET extensiblity module
    so that it can be properly handled during hibernate and resume from
    hibernate.

Arguments:
    None.

Return Value:
    None.
--*/

```

This routine is called by the system before hibernate so that it can properly register the code used by the KDNET extensibility module with the system.  This allows the system to properly manage that memory during hibernate and resume from hibernate.  (The memory gets saved late, and loaded early, since it will be called very early during resume.)

### KdInitializeController

```cpp
NTSTATUS

KdInitializeController(

    __in PVOID Adapter

    )

/*++
Routine Description:

    This function initializes the Network controller.  The controller is setup
    to send and recieve packets at the fastest rate supported by the hardware
    link.  Packet send and receive will be functional on successful exit of
    this routine.  The controller will be initialized with Interrupts masked
    since all debug devices must operate without interrupt support.

Arguments:

    Adapter - Supplies a pointer to the debug adapter object.

Return Value:
    STATUS_SUCCESS on successful initialization.  Appropriate failure code if
    initialization fails.
--*/

```

This routine is called to initialize the hardware.  It is called when the system initializes, and whenever the system wakes from a low power state for which it called KdShutdownController.  This routine MUST ensure that the hardware has fully completed initialization and that it is ready to send packets BEFORE returning.  This routine should wait for the PHY to come up, and for link to be established.  Note that if there is no cable connected, this routine should not stall indefinitely.  This routine sets the link speed and duplex in the KDNET shared data structure that is shared between KDNET and this extensibility module.  It also writes the MAC address used by the hardware, into the location pointed to by TargetMacAddress in the KDNET shared data structure.

### KdShutdownController

```cpp
VOID

KdShutdownController (

    __in PVOID Adapter

    )

/*++
Routine Description:

    This function shuts down the Network controller.  No further packets can
    be sent or received until the controller is reinitialized.

Arguments:

    Adapter - Supplies a pointer to the debug adapter object.

Return Value:

    None.
--*/
```

It is CRITICAL that this routine WAIT until all transmit packets that still pending actually get sent out on the wire.  This routine needs to wait until all transmit packets have been DMA’ed from main memory and are out on the wire BEFORE it shuts down transmit on the hardware.  Once all pending transmit packets have been sent, this routine should completely shutdown the hardware.  This routine will be called when the system shuts down, and also when the system decides to power manage the debug transport to a low power state.  This can be called when the system goes into standby, hibernate, sleep, and connected standby, in addition to when the system is shutdown.

### KdGetHardwareContextSize

```cpp
ULONG

KdGetHardwareContextSize (

    __in PDEBUG_DEVICE_DESCRIPTOR Device

    )
 

/*++
Routine Description:

    This function returns the required size of the hardware context in bytes.

Arguments:

    Device - Supplies a pointer to the debug device descriptor.

Return Value:

    None.

--*/
```

This routine should return the number of bytes required for all of the memory needed to support your hardware.  This includes your context structure, and all packet buffers for receive and transmit, as well as any hardware packet descriptors and other structures.  The size of ALL memory that you require needs to be reported here.  Including any extra memory required for alignment limitations your hardware may have for packets, or packet descriptors or other structures.

Note that this routine should be called by your KdInitializeLibrary routine when it sets the Memory Length field in the debug device descriptor.

### KdGetRxPacket

```cpp
NTSTATUS

KdGetRxPacket (

    __in PVOID Adapter,

    __out PULONG Handle,

    __out PVOID *Packet,

    __out PULONG Length

)

/*++

Routine Description:

    This function returns the next available received packet to the caller.

Arguments:

    Adapter - Supplies a pointer to the debug adapter object.

    Handle - Supplies a pointer to the handle for this packet.  This handle
        will be used to release the resources associated with this packet back
        to the hardware.

    Packet - Supplies a pointer that will be written with the address of the
        start of the packet.

    Length - Supplies a pointer that will be written with the length of the
        received packet.

Return Value:

    STATUS_SUCCESS when a packet has been received.
    STATUS_IO_TIMEOUT otherwise.

--*/
```

This routine gets the next available packet that has been received, but not yet processed.  It returns a handle for that packet.  The handle will be used to get the address of the packet by calling KdGetPacketAddress, as well as the length by calling KdGetPacketLength.  The packet and handle must remain available and valid until the packet is released by calling KdReleaseRxPacket.  This routine also directly returns the packet address and length to the caller.

If no packet is currently available this routine MUST return immediately with STATUS_IO_TIMEOUT.  This routine MUST NOT wait for a packet to be received.  Note that the top 2 bits of Handle are reserved.  TRANSMIT_HANDLE and TRANSMIT_ASYNC must both be clear.

### KdReleaseRxPacket 

```cpp
VOID

KdReleaseRxPacket (

    __in PVOID Adapter,

    ULONG Handle

)

/*++

Routine Description:

    This function reclaims the hardware resources used for the packet
    associated with the passed Handle.  It reprograms the hardware to use those
    resources to receive another packet.

Arguments:

    Adapter - Supplies a pointer to the debug adapter object.
    Handle - Supplies the handle of the packet whose resources should be
        reclaimed to receive another packet.

Return Value:

    None.

--*/
```

This routine releases the resources associated with the packet Handle back to the hardware so they can be used to receive another packet.  Every call to KdGetRxPacket that succeeds will be followed by another call to KdReleaseRxPacket with the handle returned from KdGetRxPacket.  Note that it is NOT guaranteed that KdReleaseRxPacket will be called immediately after KdGetRxPacket succeeds.  It is possible that another KdGetRxPacket call will be made first.  However, every successful KdGetRxPacket call, will have its resources released with a KdReleaseRxPacket call.

This routine should properly program the hardware so the released resources can be used to receive another packet.

### KdGetTxPacket
 
```cpp
NTSTATUS

KdGetTxPacket (

    __in PVOID Adapter,

    __out PULONG Handle

)

/*++

Routine Description:

    This function acquires the hardware resources needed to send a packet and
    returns a handle to those resources.

Arguments:

    Adapter - Supplies a pointer to the debug adapter object.

    Handle - Supplies a pointer to the handle for the packet for which hardware
        resources have been reserved.

Return Value:

    STATUS_SUCCESS when hardware resources have been successfully reserved.
    STATUS_IO_TIMEOUT if the hardware resources could not be reserved.
    STATUS_INVALID_PARAMETER if an invalid Handle pointer or Adapter is passed.

--*/
```

This routine gets the next available transmit resources and returns a handle to them.  This handle will be used to call KdGetPacketAddress, and KdGetPacketLength.  The packet address returned by KdGetPacketAddress will be used to directly write the contents of the packet.  The packet address must be the start of the packet, and the length should be the maximum number of bytes that can be written into the packet.  Note that if there are no available hardware resources, because they have all been acquired, and have not yet been transmitted, then this routine should immediately return STATUS_IO_TIMEOUT.

TRANSMIT_HANDLE must be set in the returned handle.  Note that the top two bits of Handle are reserved for the TRANSMIT_ASYNC and TRANSMIT_HANDLE flags.

### KdSendTxPacket

```cpp
NTSTATUS

KdSendTxPacket (

    __in PVOID Adapter,

    ULONG Handle,

    ULONG Length

)

/*++

Routine Description:

    This function sends the packet associated with the passed Handle out to the
    network.  It does not return until the packet has been sent.

Arguments:

    Adapter - Supplies a pointer to the debug adapter object.

    Handle - Supplies the handle of the packet to send.

    Length - Supplies the length of the packet to send.

Return Value:

    STATUS_SUCCESS when a packet has been successfully sent.

    STATUS_IO_TIMEOUT if the packet could not be sent within 100ms.

    STATUS_INVALID_PARAMETER if an invalid Handle or Adapter is passed.

--*/
```

This routine sends the packet associated with the passed handle out onto the wire.  Note that Handle may have an additional bit set in it, that indicates whether the send is an asynchronous transfer or not.  If the TRANSMIT_ASYNC flag is set in the handle, then this routine should program the hardware to send the packet, and should then immediately return without waiting for the hardware to complete the send.  This means that any errors that occur during transmit will be lost.  That is OK, and by design, as packets can be lost on the wire anyway.  If the TRANSMIT_ASYNC flag is not set in the Handle, then this routine MUST wait until the packet has been sent out on the wire, and should return any error that occurs during transmit if any.  Note that when dump files are being sent to the debugger host, or when Windows networking packets are being sent from KDNIC through KDNET, then TRANSMIT_ASYNC will be set.  When all other debugger packets are being sent TRANSMIT_ASYNC will be clear.

If a set of packets are sent with TRANSMIT_ASYNC set TRUE, followed by a packet that does not have TRANSMIT_ASYNC set, the hardware must wait until the packet without the flag set, is actually sent, even if this means it has to wait for the previous async packets to be sent also.

### KdGetPacketAddress 
 
```cpp
PVOID

KdGetPacketAddress (

    __in PVOID Adapter,

    ULONG Handle

)

/*++

Routine Description:

    This function returns a pointer to the first byte of a packet associated
    with the passed handle.

Arguments:

    Adapter - Supplies a pointer to the debug adapter object.

    Handle - Supplies a handle to the packet for which to return the
        starting address.

Return Value:

    Pointer to the first byte of the packet.

--*/
```

This routine returns a pointer to the first byte of the packet associated with the passed Handle.  Note that the Handle will have the TRANSMIT_HANDLE bit set for transmit packets, and the TRANSMIT_HANDLE bit clear for receive packets.  The returned pointer should be a Windows virtual address that can be read or written by the processor.  This address should fall within the memory block reserved for the KDNET extensibility module which is passed in the debug device descriptor Memory structure.  (Note that the KDNET extensibility module should NEVER use more than the memory size it requested in KdInitializeLibrary when accessing that memory.  Any additional memory at the end of the block is reserved for use by KDNET, and must not be touched by the KDNET extensibility module.)

### KdGetPacketLength

```cpp
ULONG

KdGetPacketLength (

    __in PVOID Adapter,

    ULONG Handle

)

/*++

Routine Description:

    This function returns the length of the packet associated with the passed
    handle.

Arguments:

    Adapter - Supplies a pointer to the debug adapter object.

    Handle - Supplies a handle to the packet for which to return the
        length.

Return Value:

    The length of the packet.

--*/
```

This routine returns a length in bytes of the packet associated with the passed Handle.  Note that the Handle will have the TRANSMIT_HANDLE bit set for transmit packets, and the TRANSMIT_HANDLE bit clear for receive packets.  For transmit packets, this length should be the maximum number of bytes that can be written to the packet.  For receive packets, this length should be the actual number of bytes in the received packet.

## Debugging KDNET Extensibility Modules

To debug a KDNET extensibility module you need to run the following bcdedit commands from an elevated command prompt on the target machine.

First, and most important, you need to run the following two commands to make sure that Winload will allow repeated boot failures without going down a special failure path that breaks into the debugger and prevents normal boot.  Running these commands will allow you to repeatedly reboot the machine with new bits, and debug those new bits without issue.

`Bcdedit -set {current} BootStatusPolicy IgnoreAllFailures`

`Bcdedit -set {current} RecoveryEnabled No`

Assuming you will use serial debugging on com1 on the target machine to debug the extensibility module, do the following.

`bcdedit -dbgsettings serial debugport:1 baudrate:115200`

This sets the default debug transport to serial on com1 at 115200 baud.  These settings will be used for boot debugging also.

`bcdedit -debug on`

This enables kernel debugging.

`bcdedit -bootdebug on`

This enables boot debugging on winload.exe, which you will use to debug into the early kernel initialization including your KDNET extensibility module.

`bcdedit -set kerneldebugtype net`

This forces the kernel debug type to net, regardless of the default debug transport settings.  This will cause winload.exe to load kdnet.dll as the kernel debug transport.

`bcdedit -set kernelbusparams b.d.f`

Where b is the bus number, d is the device number and f is the function number – all in decimal – of the hardware you are writing the KDNET extensiblity module for.  These numbers will depend on which PCI slot the hardware is located in.  You can find these by finding the location string in the device properties page of the network device in Windows device manager.  Open Windows device manager, double click on network devices, find your device, double click on it, and in the window that opens there should be a Location:  field that contains the bus, device and function of the hardware on the PCI bus.  If you have a bus driver that causes that information to be masked, then you will have to determine the location from your drivers, or some other way.

This forces the kernel busparams to b.d.f – which forces that particular device to be selected as the kernel debug device.

`bcdedit -set kernelhostip N`

Where N is determined by the following formula.  If your host debugger machine has an IPv4 address of w.x.y.z, then N = (w*0x01000000) + (x*0x00010000) + (y*0x00000100) + (z*0x00000001).  N needs to be specified on the command line in decimal, not hex.  Effectively you take each byte of the IPv4 address and you concatenate it (in hex) to build a 32 bit number in hex, and then you convert that to decimal.

`bcdedit -set kernelport N`

Where N is 50000 or some other port that will not be blocked on your internal network.

This forces KDNET to use port N as the network debug port.

`bcdedit -set kernelkey 1.2.3.4`

This forces the KDNET debug key to 1.2.3.4.  1.2.3.4 is not a secure or unique on the network key. To keep the target computer secure, packets that travel between the host and target computers must be encrypted. We strongly recommend that you use an automatically generated encryption key. For more information, see [Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md).

`bcdedit -set kerneldhcp on`

This forces the KDNET kernel dhcp setting to on.

Run your debugger on the debugger host machine with the following command line assuming that you are using com1 as your serial debug port on the host machine:

`windbg -d -k com:port=com1,baud=115200`

That will run the debugger and will cause it to breakin when the windbg boot debugger first communicates with the host machine.

Then reboot the target machine by running

`shutdown -r -t 0`

When the debugger breaks into windbg, make sure you get symbols loaded for winload.  (might need to set the .sympath and do a .reload). Then run `x winload!*deb*tra*`. One of the symbols listed will be something like BdDebugTransitions.

Then run `ed winload!BdDebugTransitions 1`, but make sure to use the correct symbol name.

Then run, `bu winload!blbdstop` to set a breakpoint.

Then hit `g` to go.

You should break in at winload!BlBdStop.

Then, run the following commands.

`bu nt!KdInitSystem`

`bu kdnet!KdInitialize`

`bu kdstub!KdInitializeLibrary`

Note that most likely you will use kdstub when setting breakpoints in your KDNET extensibility module, if that doesn’t work then use

`bu kd_YY_XXXX!KdInitializeLibrary`

Where YY is your PCI class, and XXXX is your PCI VID.  (ie: Use the name of your KDNET extensibility module.)

Usually in the debugger you will need to use kdstub instead of using the actual name of your extensibility module.

Then run `bl` to list the breakpoints. Make sure the breakpoints are in place (they should all have an e next to them).

Then hit `g`. You should hit the nt!KdInitSystem breakpoint.

Hit `g` again, and you should hit kdnet!KdInitialize

Hit `g` again and you should hit a breakpoint in your own module at KdInitializeLibrary.

Then you can set a breakpoint on your InitializeController routine, as well as all your other routines, and step through your code.

Once you step through KdInitializeLibrary, hit g, and if you set a breakpoint on your InitializeController routine, that will get hit next.

Then once that completes, make sure you have breakpoints set on your KdGetTxPacket, KdSendTxPacket, KdGetRxPacket, KdReleaseRxPacket routines, and hit g again, and those routines will get run as part of network initialization done by KDNET during boot.

You may need to add temporary code to your KdInitializeLibrary or KdInitializeController routines to make sure that all of your routines get called so that you can step through all of your code.  (KdShutdownController for example won’t get called during startup when things work normally, so you will need to explicitly call it from temporary code so that you can step through it and make sure it is correct.)

Once you have stepped through all of your code and are confident it is correct, then reboot the target, but do NOT set the winload!BdDebugTransitions flag to true (leave it defaulted to zero).

Then also run another instance of the kernel debugger on your host debugger machine.

`Windbg -d -k net:port=50000,key=1.2.3.4`

Let the target machine boot, and it should connect to the other instance of the kernel debugger over the network.

Then run commands in the kernel debugger and make sure it works, and then let the target continue booting, and make sure you can later break in and run commands.

> [!NOTE]
> Setting the debug transitions flag in winload, guarantees that Windows WILL NOT BOOT.  If you attempt to allow Windows to finish booting after setting that flag, Windows will simply crash, or hang.  If you want Windows to boot successfully you cannot set that debug transitions flag.  Setting the flag allows you to debug your code, and verify that it is correct, by stepping through it in the debugger, but ultimately you will need to not set the flag so that you can verify that debugging works when you boot normally.  This means that you cannot step through your code when booting the system normally, and in fact, when Windows is running normally, with debugging enabled on your hardware, your KDNET extensibility module is un-debug-able.  Any attempt to debug it with the kernel debugger, will cause the machine to crash.  (You cannot set breakpoints in code that runs in the kernel debug paths, as it causes infinite reentry, a blown stack, and a reboot.)

## Multiple Physical Functions - 2PF

In addition to KDNET extensibility, KDNET supports kernel debugging using multiple Physical Functions (PFs) on the supported NICs by partitioning the PCI configuration space. Network card vendors are encouraged to enable support for this feature. For more information, see [Debugger 2PF KDNET Miniport Network Driver Support](../network/debugger-2pf-kdnet-support.md).

## Related topics

[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)

[Setting Up KDNET Network Kernel Debugging Manually](setting-up-a-network-debugging-connection.md)

[Debugger 2PF KDNET Miniport Network Driver Support](../network/debugger-2pf-kdnet-support.md)
