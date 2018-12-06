---
title: AV/C Connection Scenarios
description: AV/C Connection Scenarios
ms.assetid: 392f996c-47aa-4ceb-adf9-0c8fd114a511
keywords:
- connections WDK AV/C
- AV/C WDK , connection scenarios
- digital video WDK AV/C
- DV WDK AV/C
- Set-Top Box WDK AV/C
- STB WDK AV/C
- TV WDK AV/C
- television WDK AV/C
- subunit support WDK AV/C
- intra-unit connections WDK AV/C
- inter-unit connections WDK AV/C
- Avc.sys function driver WDK , connections
- external plug connections WDK AV/C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AV/C Connection Scenarios





Before Windows Vista, the Connection and Compatibility Management (CCM) protocol in *Avc.sys* supported a single connection scenario, in which the computer acted as a controller for an external AV/C device to initiate data streaming from the device. For example, to begin streaming, the connection management in *Avc.sys* established a connection between a subunit on the device and the isochronous output plug of the device unit by using the connect and disconnect unit commands ([**AVC\_FUNCTION\_ACQUIRE**](https://msdn.microsoft.com/library/windows/hardware/ff554148) and [**AVC\_FUNCTION\_RELEASE**](https://msdn.microsoft.com/library/windows/hardware/ff554169), respectively). For more information about the AV/C specification and the CCM protocol, see the [1394 Trade Association](http://go.microsoft.com/fwlink/p/?linkid=518448) website.

In Windows Vista, the connection management has been improved to support seven more connection scenarios, so that *Avc.sys* supports eight unit/subunit connection scenarios. The connection management improvements add support for connections from subunit plugs to other subunit plugs; the subunits can be within the same AV/C unit or in different AV/C units. *Avc.sys* establishes connections by using the signal-source and then input-select CCM protocol unit commands. (*Avc.sys* supports other CCM protocol unit commands, such as output-preset, only to the level that the AV/C specification requires.)

There are two general types of connections that relate to AV/C units and subunits:

-   *A connection in which an external device connects to the host computer and the computer can control the connection but it is not part of the connection*. This connection type does not use any host-based memory. Instead, the connection is a memory-less medium with a device and the host simply acts as a controller. An example of this type of connection is a tuner subunit of a Set-Top Box (STB) that streams data directly to the monitor subunit of a digital TV, without the computer processing the data stream.

-   *A connection in which an external device connects to the host computer by using a standard medium and uses buffers to copy data from the device to the host computer's memory*. An example of this type of connection is a digital video (DV) device that streams data to the computer, where it is later processed. The *Msdv.sys* driver uses this type of connection (between the DV device and the host computer).

The improved connection management that is implemented for Windows Vista in *Avc.sys* applies to the first type of connection, in which the device can respond to the AV/C command to make internal connections. The improved connection management in *Avc.sys* can establish an end-to-end connection between two tape subunits in different AV/C devices (on the same IEEE 1394 bus), if the devices support the AV/C CCM protocol.

**Note**  *Avc.sys* does not support the second type of connection (memory-buffer). However, the memory-buffer type of connection follows the [IEC 61883](https://msdn.microsoft.com/library/windows/hardware/ff537188) protocol and is supported by the underlying *61883.sys* driver in the same stack (where the computer is involved in memory-buffer connections).

 

### Supported Connection Scenarios in Windows Vista

Four scenarios (1 through 4) represent *intra*-unit connections. These connections are contained completely within in one AV/C unit. Four other scenarios (5 through 8) represent *inter*-unit connections. These connections are between two different AV/C units.

The following topics discuss the eight different AV/C connection management scenarios and the respective values for the members of the [**AVCCONNECTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff554101) structure:

[Connections Between Subunit Plugs and Unit Plugs Within One AV/C Unit](connections-between-subunit-plugs-and-unit-plugs-within-one-av-c-unit.md)

[Connections Between Two Subunit Plugs Within One AV/C Unit](connections-between-two-subunit-plugs-within-one-av-c-unit.md)

[Connections Between Two Subunit Plugs in Different AV/C Units](connections-between-two-subunit-plugs-in-different-av-c-units.md)

[Connections Between Two Unit Plugs in Different AV/C Units](connections-between-two-unit-plugs-in-different-av-c-units.md)

 

 




