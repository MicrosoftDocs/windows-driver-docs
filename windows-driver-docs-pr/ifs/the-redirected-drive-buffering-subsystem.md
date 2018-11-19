---
title: The Redirected Drive Buffering SubSystem
description: The Redirected Drive Buffering SubSystem
ms.assetid: 901a8b3e-222a-44be-8279-765d8ec4ffe1
keywords:
- network redirectors WDK , RDBSS
- redirector drivers WDK , RDBSS
- Redirected Drive Buffering SubSystem WDK file systems
- RDBSS WDK file systems
- mini-redirectors WDK , RDBSS
- non-monolithic drivers WDK
- buffering code WDK network redirectors
- I/O WDK network redirectors
- kernel network redirectors WDK , RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The Redirected Drive Buffering SubSystem


## <span id="ddk_the_redirected_drive_buffering_subsystem_if"></span><span id="DDK_THE_REDIRECTED_DRIVE_BUFFERING_SUBSYSTEM_IF"></span>


The Redirected Drive Buffering SubSystem (RDBSS) is provided as a kernel-mode file system driver, *rdbss.sys*, which is included with the operating system and as a static library, *rdbsslib.lib*, which is included with the Windows Driver Kit (WDK). The static library duplicates the code in the *rdbss.sys* kernel-mode driver.

The original scheme was that all network mini-redirectors would link dynamically with the *rdbss.sys* kernel driver. Drivers that linked dynamically to *rdbss.sys* are called non-monolithic drivers. However, this feature was never fully implemented, so only the Microsoft SMB network mini-redirector links dynamically to *rdbss.sys* and is a non-monolithic driver. All other network mini-redirectors, including other Microsoft redirectors included with the operating system, link against the *rdbsslib.lib* library and statically include the same code as the *rdbss.sys* kernel driver. While the same RDBSS source code is used in both the *rdbss.sys* driver and the *rdbsslib.lib* library, the size of a monolithic network mini-redirector driver is larger since most of the code in *rdbss.sys* is included with each driver. For example, on Windows Server 2003, the file sizes for various drivers are as follows:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Driver</th>
<th align="left">File Size</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>rdbss.sys</em></p></td>
<td align="left"><p>156 KB</p></td>
<td align="left"><p>The RDBSS device driver used only by the Microsoft SMB mini-redirector.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>mrxdav.sys</em></p></td>
<td align="left"><p>179 KB</p></td>
<td align="left"><p>The Microsoft WebDAV network mini-redirector driver, which links in much of <em>rdbsslib.lib</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>rdrpdr.sys</em></p></td>
<td align="left"><p>185 KB</p></td>
<td align="left"><p>The Microsoft Terminal Services network mini-redirector driver, which links in much of <em>rdbsslib.lib</em>.</p></td>
</tr>
</tbody>
</table>

 

The RDBSS communicates with the I/O Manager, Cache Manager, Memory Manager, network mini-redirectors, and other kernel systems. RDBSS supports the following features:

-   A well-defined mechanism is defined for communication between RDBSS and mini-redirector drivers.

-   Multiple buffering modes are supported. There are also support routines to help the network mini-redirector change the buffering modes dynamically to enable live sharing.

-   The network mini-redirector can indicate support for various options, including case-sensitive names, UNC naming, printing, pipes, mailslots, and scavenging (reusing some data structures).

-   The network mini-redirector provides support for namespace, file information, and connection caching to reduce unnecessary network operations.

The RDBSS uses a well-defined mechanism for communication. RDBSS exports a large number of functions that can be called by a mini-redirector driver and other kernel systems to set options and perform various operations.

A mini-redirector implements a number of call-back functions that are used by RDBSS to communicate with the mini-redirector driver. When a mini-redirector driver first starts (in its **DriverEntry** routine), the driver calls an RDBSS function for registering mini-redirector drivers and passes in a structure with pointers to these callback functions (dispatch table) along with some configuration data values.

The callback functions that must be implemented in a mini-redirector driver fall into the following basic categories:

-   Callbacks to manage network mini-redirector data structures.

-   Callbacks for file I/O operations.
    -   Synchronous file I/O routines (create, close, and cleanup, for example).
    -   Asynchronous file I/O routines (read, write. FSTCL, IOCTL, and lock, for example). For historical reasons, these synchronous file I/O routines in a network mini-redirector were often called low I/O operations.

The file I/O callbacks are expected to be synchronous, except for the functions that fall in the low I/O category. The low I/O routines can operate asynchronously and therefore must support cancellation.

RDBSS and mini-redirectors commonly use a fundamental data structure, the RX\_CONTEXT, to pass information. The RX\_CONTEXT encapsulates a large amount of information and includes a pointer to the current IRP. There is a default size for this RX\_CONTEXT data structure. The size of this RX\_CONTEXT structure can be extended based on the requirements of the remote file system and network mini-redirector. The size to use for this extended RX\_CONTEXT is defined when a mini-redirector first registers with RDBSS (one of the data values specified).

RDBSS and mini-redirectors also make extensive use of the following data structure abstractions:

-   Server Call Context (SRV\_CALL)--The context associated with each known file system server.

-   Net Roots (NET\_ROOT)--The root of a share opened by the user.

-   Virtual Net Roots (V\_NET\_ROOT)--The view of a share on a server. The view can be constrained along multiple dimensions. As an example the view can be associated with a logon ID, which constrains the operations that can be performed on the share.

-   File Control Blocks (FCB)--The RDBSS data structure associated with each unique file opened on the client.

-   File Object Extensions (FOBX)--The RDBSS extension to the NT FILE\_OBJECT.

-   ServerSide Open Context (SRV\_OPEN)--The open handle to a file on a remote share.

RDBSS has very flexible support for buffering. RDBSS can be set to separately buffer read and write requests. File size and file time can also be cached. Explicit buffering strategies are allowed and these can be set when a share on a file server is opened. Buffering can also be set on an individual file basis.

RDBSS will try to use access history to reduce the need for unnecessary network requests. For example, if an open request for a remote file fails, this information will be cached by RDBSS. If the client immediately requests to open a similar file, with a change of case in the file name, RDBSS will fail the request for remote file systems that ignore case in file names.

 

 




