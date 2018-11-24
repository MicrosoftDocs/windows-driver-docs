---
title: Peer Subunit Driver Stack
description: Peer Subunit Driver Stack
ms.assetid: 6ef4b6ae-3802-4ba9-acfa-4b3edba11ba3
keywords:
- peer subunit driver stacks WDK AV/C
- driver stacks WDK AV/C
- stacks WDK AV/C
- subunit support WDK AV/C
- AV/C WDK , driver stacks
- unit commands WDK AV/C
- built-in extension mechanism WDK AV/C
- command extension mechanism WDK AV/C
- command targets WDK AV/C
- Avc.sys function driver WDK , driver stacks
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Peer Subunit Driver Stack


The peer driver stack consists of the drivers loaded to represent AV/C subunits that are active on the IEEE 1394 bus and that can be controlled from the computer. External device control must be initiated through the AV/C peer driver stack. Windows loads an instance of *Avc.sys* for each external AV/C device on the IEEE 1394 bus whenever a device is connected to the system (or present during the system startup). Each instance of *Avc.sys* that is loaded to support a peer subunit driver registers a new instance of the GUID\_AVC\_CLASS device interface. For more information about the GUID\_AVC\_CLASS device interface, see [Using Avc.sys](using-avc-sys.md) and [**IOCTL\_AVC\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff560789).

Peer subunit drivers access and control their subunits through the IOCTL\_AVC\_CLASS interface that is exported by *Avc.sys*. *Avc.sys* handles the AV/C command and response protocol, including all interaction with the IEC 61883 Function Control Protocol (FCP). However, note that a peer subunit driver is not prevented from communicating with and directly accessing certain *61883.sys* functionality when necessary. A subunit driver might need to communicate directly with *61883.sys* when the subunit driver represents an AV/C subunit that uses a stream format that Microsoft does not support. A subunit driver can use the **IOCTL\_61883\_CLASS** interface to communicate directly with *61883.sys* when necessary. Microsoft supplies the lower-filter driver, *Avcstrm.sys*, which can assist with streaming DV and MPEG2 formats. For more information about *Avcstrm.sys*, see [AV/C Streaming Overview](av-c-streaming-overview.md).

A peer subunit driver can register to be notified of and receive AV/C commands from external AV/C devices. To register, a peer subunit driver issues an [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) I/O request packet (IRP) with the **IoControlCode** member of the IOCTL\_AVC\_CLASS I/O control code and the subfunction set to AVC\_FUNCTION\_GET\_REQUEST. This functionality allows a peer subunit driver to receive AV/C requests from its subunit and enables support for specifications, such as the Connection and Compatibility Management (CCM) protocol and Digital Transmission Content Protection (DTCP).. For more information about CCM, see the [IEEE 1394 Trade Association](http://go.microsoft.com/fwlink/p/?LinkId=518448) website. For more information about DTCP, see the [Digital Transmission Licensing Administrator](http://go.microsoft.com/fwlink/p/?linkid=8731) website.

Note that this functionality is intended to support a virtual AV/C subunit driver to send AV/C commands to the computer (where the subunit driver is located in the virtual AV/C device stack) and not to permit AV/C subunits on external devices to send AV/C commands to the computer system.

### <a href="" id="peer-stack-as-av-c-command-target"></a>**Peer Stack as AV/C Command Target**

The peer subunit driver stack can contain additional WDM filter drivers that provide vendor-specific or device-specific target AV/C functionality. Through this peer subunit driver stack extension mechanism, third-party vendors can independently implement value-added features such as 5C copy protection, as well as extensions to the AV/C implementation provided by Microsoft.

Subunit drivers can perform this function, but for devices with multiple subunits, a WDM filter driver is the preferred method. The computer is only exposed as an AV/C target if an upper driver (subunit or filter driver) registers to receive incoming requests through [**AVC\_FUNCTION\_GET\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff554163). For more information about AV/C unit commands, see [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145).

Driver loading is based on device identifiers (IDs); therefore, unit functionality can be loaded selectively on a device-specific or vendor-specific basis. The virtual subunit driver stack supports this mechanism generically (not in a device-specific way).

Note that if the peer subunit driver stack implements device-specific unit extensions, any unhandled unit commands, as well as all incoming subunit commands, are routed to the [virtual subunit driver stack](virtual-subunit-driver-stack.md).

### **Unit Command Extension Mechanism**

In the context of the peer subunit driver stack, target functionality is limited to the support of AV/C unit commands. If a subunit driver (for a virtual subunit or peer subunit) registers to receive AV/C requests, then *Avc.sys* supports only SUBUNIT\_INFO (0x31) and UNIT\_INFO (0x30) opcodes directly. For more information about opcodes, see the *AV/C Digital Interface Command Set General Specification, Rev 3.0*. To support additional unit commands, such as those for the CCM protocol or DTCP, *Avc.sys* provides a plug-in extension mechanism. Any number of subunit or WDM filter drivers can register the unit opcodes that they support through the **AlternateOpcodes** member of the [**AVC\_COMMAND\_IRB**](https://msdn.microsoft.com/library/windows/hardware/ff554140) structure that was submitted through the [**AVC\_FUNCTION\_GET\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff554163) function. **AlternateOpcodes** is a counted byte array; element 0 is the number of alternate opcodes in the remaining bytes. **AlternateOpcodes** is ignored when sending a response, so the alternate opcodes do not need to be hidden when processing a unit request.

To use the built-in extension mechanism, specify the unit address as 0xff in the **SubunitAddress** member of the AVC\_COMMAND\_IRB structure. The **SubunitAddress** member is left alone in for unit commands (the unit address provided by the subunit driver still exists). The virtual subunit driver is always able to key off of the **SubunitAddress** member.

 

 




