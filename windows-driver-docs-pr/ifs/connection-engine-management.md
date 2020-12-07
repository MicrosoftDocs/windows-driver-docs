---
title: Connection Engine Management
description: Connection Engine Management
keywords:
- RDBSS WDK file systems , connection engine management
- Redirected Drive Buffering Subsystem WDK file systems , connection engine management
- connection engine WDK network redirectors
- TDI drivers WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceallocateirpwithmdl" data-raw-source="[&lt;strong&gt;RxCeAllocateIrpWithMDL&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceallocateirpwithmdl)"><strong>RxCeAllocateIrpWithMDL</strong></a></p></td>
<td align="left"><p>This routine allocates an IRP for use by the connection engine and associates an MDL with the IRP.</p>
<p>This routine is only available on Windows XP.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildaddress" data-raw-source="[&lt;strong&gt;RxCeBuildAddress&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildaddress)"><strong>RxCeBuildAddress</strong></a></p></td>
<td align="left"><p>This routine associates a transport address with a transport binding.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildconnection" data-raw-source="[&lt;strong&gt;RxCeBuildConnection&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildconnection)"><strong>RxCeBuildConnection</strong></a></p></td>
<td align="left"><p>This routine establishes a connection between a local RDBSS connection address and a given remote address. This routine should be called in the context of a system worker thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildconnectionovermultipletransports" data-raw-source="[&lt;strong&gt;RxCeBuildConnectionOverMultipleTransports&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildconnectionovermultipletransports)"><strong>RxCeBuildConnectionOverMultipleTransports</strong></a></p></td>
<td align="left"><p>This routine establishes a connection between a local RDBSS connection address and a given remote address and supports multiple transports. A set of local addresses are specified and this routine attempts to connect to the target server through all of the transports associated with the local addresses. One connection is chosen as the winner depending on the connect options. This routine must be called in the context of a system worker thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildtransport" data-raw-source="[&lt;strong&gt;RxCeBuildTransport&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildtransport)"><strong>RxCeBuildTransport</strong></a></p></td>
<td align="left"><p>This routine binds an RDBSS transport to a specified transport name.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildvc" data-raw-source="[&lt;strong&gt;RxCeBuildVC&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcebuildvc)"><strong>RxCeBuildVC</strong></a></p></td>
<td align="left"><p>This routine adds a virtual circuit to a specified connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcecancelconnectrequest" data-raw-source="[&lt;strong&gt;RxCeCancelConnectRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcecancelconnectrequest)"><strong>RxCeCancelConnectRequest</strong></a></p></td>
<td align="left"><p>This routine cancels a previously issued connection request.</p>
<p>Note that this routine is not currently implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcefreeirp" data-raw-source="[&lt;strong&gt;RxCeFreeIrp&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcefreeirp)"><strong>RxCeFreeIrp</strong></a></p></td>
<td align="left"><p>This routine frees an IRP used by the connection engine.</p>
<p>This routine is only available on Windows XP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceinitiatevcdisconnect" data-raw-source="[&lt;strong&gt;RxCeInitiateVCDisconnect&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceinitiatevcdisconnect)"><strong>RxCeInitiateVCDisconnect</strong></a></p></td>
<td align="left"><p>This routine initiates a disconnect on the virtual circuit. This routine must be called in the context of a system worker thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcequeryadapterstatus" data-raw-source="[&lt;strong&gt;RxCeQueryAdapterStatus&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcequeryadapterstatus)"><strong>RxCeQueryAdapterStatus</strong></a></p></td>
<td align="left"><p>This routine returns the ADAPTER_STATUS structure for a given transport.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcequeryinformation" data-raw-source="[&lt;strong&gt;RxCeQueryInformation&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcequeryinformation)"><strong>RxCeQueryInformation</strong></a></p></td>
<td align="left"><p>This routine queries information that pertains to a connection.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcequerytransportinformation" data-raw-source="[&lt;strong&gt;RxCeQueryTransportInformation&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcequerytransportinformation)"><strong>RxCeQueryTransportInformation</strong></a></p></td>
<td align="left"><p>This routine returns the transport information about the connection count and quality of service for a given transport.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcesend" data-raw-source="[&lt;strong&gt;RxCeSend&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcesend)"><strong>RxCeSend</strong></a></p></td>
<td align="left"><p>This routine sends a TSDU along the specified connection on a virtual circuit.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcesenddatagram" data-raw-source="[&lt;strong&gt;RxCeSendDatagram&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxcesenddatagram)"><strong>RxCeSendDatagram</strong></a></p></td>
<td align="left"><p>This routine sends a TSDU to a specified transport address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardownaddress" data-raw-source="[&lt;strong&gt;RxCeTearDownAddress&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardownaddress)"><strong>RxCeTearDownAddress</strong></a></p></td>
<td align="left"><p>This routine removes a transport address from a transport binding.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardownconnection" data-raw-source="[&lt;strong&gt;RxCeTearDownConnection&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardownconnection)"><strong>RxCeTearDownConnection</strong></a></p></td>
<td align="left"><p>This routine tears down a given connection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardowntransport" data-raw-source="[&lt;strong&gt;RxCeTearDownTransport&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardowntransport)"><strong>RxCeTearDownTransport</strong></a></p></td>
<td align="left"><p>This routine unbinds from the transport specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardownvc" data-raw-source="[&lt;strong&gt;RxCeTearDownVC&lt;/strong&gt;](/windows-hardware/drivers/ddi/rxce/nf-rxce-rxceteardownvc)"><strong>RxCeTearDownVC</strong></a></p></td>
<td align="left"><p>This routine tears down a virtual connection.</p></td>
</tr>
</tbody>
</table>

 

**Note**   TDI will not be supported in Microsoft Windows versions after Windows Vista. Use [Windows Filtering Platform](../network/windows-filtering-platform-callout-drivers2.md) or [Winsock Kernel](/windows-hardware/drivers/ddi/_netvista/) instead.

 

