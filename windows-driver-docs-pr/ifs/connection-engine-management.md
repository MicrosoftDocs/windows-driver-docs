---
title: Connection Engine Management
description: Connection Engine Management
ms.assetid: 00ac74c5-2a69-493f-ad9b-6fa2f9082ac1
keywords: ["RDBSS WDK file systems , connection engine management", "Redirected Drive Buffering Subsystem WDK file systems , connection engine management", "connection engine WDK network redirectors", "TDI drivers WDK file systems"]
---

# Connection Engine Management


## <span id="ddk_connection_engine_management_if"></span><span id="DDK_CONNECTION_ENGINE_MANAGEMENT_IF"></span>


In RDBSS, the connection engine is designed to map and emulate the TDI specifications as closely as possible. This provides an efficient mechanism that fully exploits the underlying TDI implementation for use by network mini-redirectors.

While the RDBSS connection engine does abstract TDI, network redirectors are also free to communicate directly with TDI instead of using these RDBSS connection engine routines. The existing RDBSS connection engine routines that provide wrappers for TDI were developed to support Microsoft Networks, so they are very Windows-centric and may not be appropriate for other network directors. Also, the connection engine routines in RDBSS are to be removed from Windows operating systems released after Windows Server 2003. In the future, each network redirector will be responsible for developing the connection engine routines needed (to TDI or some other transport). For example, a WebDAV redirector could talk to some user-mode reflector process to send out HTTP packets (standard TCP/IP) rather than TDI.

The RDBSS connection engine routines deal with the following entities:

-   Transports

-   Transport addresses

-   Transport connections

-   Virtual circuits on a connection

The transports are bindings to the various transport service providers on any system. The transport addresses are the local connection end points. The connections are transport connections between endpoints. Each connection encapsulates a number of virtual circuits (typically one).

The following important data structures are created and manipulated by the various connection engine routines associated with RDBSS:

-   RXCE\_TRANSPORT--encapsulates all of the parameters for a transport

-   RXCE\_ADDRESS--encapsulates all of the parameters for a transport address

-   RXCE\_CONNECTION--encapsulates all of the parameters for a transport connection

-   RXCE\_VC--encapsulates all of the parameters for a virtual circuit on a transport connection

Network mini-redirector drivers can use these data structures and invoke the routines provided for each type to build and tear down the connection engine portions. These routines do not allocate or free the memory associated with these structures. This provides a flexible mechanism for mini-redirector drivers to manage instances of these connection engine data structures.

The four connection engine types described above are tagged at the beginning of each data structure with a special RXCE\_SIGNATURE signature that is used extensively by RDBSS for validation.

RDBSS provides the following connection engine routines that can be used by network mini-redirector drivers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>RxCeAllocateIrpWithMDL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553405)</p></td>
<td align="left"><p>This routine allocates an IRP for use by the connection engine and associates an MDL with the IRP.</p>
<p>This routine is only available on Windows XP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeBuildAddress</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553414)</p></td>
<td align="left"><p>This routine associates a transport address with a transport binding.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeBuildConnection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553417)</p></td>
<td align="left"><p>This routine establishes a connection between a local RDBSS connection address and a given remote address. This routine should be called in the context of a system worker thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeBuildConnectionOverMultipleTransports</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553424)</p></td>
<td align="left"><p>This routine establishes a connection between a local RDBSS connection address and a given remote address and supports multiple transports. A set of local addresses are specified and this routine attempts to connect to the target server through all of the transports associated with the local addresses. One connection is chosen as the winner depending on the connect options. This routine must be called in the context of a system worker thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeBuildTransport</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553434)</p></td>
<td align="left"><p>This routine binds an RDBSS transport to a specified transport name.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeBuildVC</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553439)</p></td>
<td align="left"><p>This routine adds a virtual circuit to a specified connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeCancelConnectRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553440)</p></td>
<td align="left"><p>This routine cancels a previously issued connection request.</p>
<p>Note that this routine is not currently implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeFreeIrp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553448)</p></td>
<td align="left"><p>This routine frees an IRP used by the connection engine.</p>
<p>This routine is only available on Windows XP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeInitiateVCDisconnect</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553454)</p></td>
<td align="left"><p>This routine initiates a disconnect on the virtual circuit. This routine must be called in the context of a system worker thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeQueryAdapterStatus</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553456)</p></td>
<td align="left"><p>This routine returns the ADAPTER_STATUS structure for a given transport.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeQueryInformation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553461)</p></td>
<td align="left"><p>This routine queries information that pertains to a connection.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeQueryTransportInformation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553474)</p></td>
<td align="left"><p>This routine returns the transport information about the connection count and quality of service for a given transport.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeSend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553479)</p></td>
<td align="left"><p>This routine sends a TSDU along the specified connection on a virtual circuit.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeSendDatagram</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553482)</p></td>
<td align="left"><p>This routine sends a TSDU to a specified transport address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeTearDownAddress</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553488)</p></td>
<td align="left"><p>This routine removes a transport address from a transport binding.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeTearDownConnection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554321)</p></td>
<td align="left"><p>This routine tears down a given connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxCeTearDownTransport</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554328)</p></td>
<td align="left"><p>This routine unbinds from the transport specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxCeTearDownVC</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554332)</p></td>
<td align="left"><p>This routine tears down a virtual connection.</p></td>
</tr>
</tbody>
</table>

 

**Note**   TDI will not be supported in Microsoft Windows versions after Windows Vista. Use [Windows Filtering Platform](https://msdn.microsoft.com/library/windows/hardware/ff571068) or [Winsock Kernel](https://msdn.microsoft.com/library/windows/hardware/ff571083) instead.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Connection%20Engine%20Management%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




