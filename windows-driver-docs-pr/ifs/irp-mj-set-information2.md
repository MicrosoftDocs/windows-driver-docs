---
title: Checking the Oplock State of an IRP_MJ_SET_INFORMATION operation
description: Checking the Oplock State of an IRP_MJ_SET_INFORMATION operation
ms.assetid: d164be8d-cf42-4b96-9883-e0f8223bfde4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Checking the Oplock State of an IRP_MJ_SET_INFORMATION operation


Certain IRP_MJ_SET_INFORMATION operations check oplock state. The following six operations perform this check:

### <span id="FileEndOfFileInformation__FileAllocationInformation__and_FileValidDataLengthInformation"></span><span id="fileendoffileinformation__fileallocationinformation__and_filevaliddatalengthinformation"></span><span id="FILEENDOFFILEINFORMATION__FILEALLOCATIONINFORMATION__AND_FILEVALIDDATALENGTHINFORMATION"></span>FileEndOfFileInformation, FileAllocationInformation, and FileValidDataLengthInformation

This information applies when the following operations are being performed on a file or stream:

- A caller attempts to change the logical size of the stream. Note that when the cache manager's lazy writer thread attempts to set a new end of file, no oplock check is made. This is because the check is made previously when the real write request is received.

- A caller attempts to change the allocated size of the stream.
  <table>
  <tr>
  <th>Request Type</th>
  <th>Conditions</th>
  </tr>
  <tr>
  <td rowspan="2">
  <p>Level 1</p>
  <p>Batch</p>
  <p>Filter</p>
  <p>Read-Handle</p>
  <p>Read-Write</p>
  <p>Read-Write-Handle</p>
  </td>
  <td>
  <p>Broken on IRP_MJ_SET_INFORMATION (for FileEndOfFileInformtion, FileAllocationInformation, and FileValidDataLengthInformation) when:</p>
  <ul>
  <li>
  <p> The operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td>
  <p>If the oplock is broken:</p>
  <ul>
  <li>
  <p> Break to None.</p>
  </li>
  <li>
  <p>For the Read-Handle request: Although acknowledgment of the break is required, the operation continues immediately (i.e., without waiting for the acknowledgment).</p>
  </li>
  <li>
  <p> For all other request types: An acknowledgment must be received before the operation continues.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td rowspan="2">
  <p>Read</p>
  </td>
  <td>
  <p>Broken on IRP_MJ_SET_INFORMATION (for FileEndOfFileInformtion, FileAllocationInformation, and FileValidDataLengthInformation) when:</p>
  <ul>
  <li>
  <p> The operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td>
  <p>If the oplock is broken:</p>
  <ul>
  <li>
  <p> Break to None.</p>
  </li>
  <li>
  <p> No acknowledgment is required, the operation proceeds immediately.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td>
  <p>Level 2</p>
  </td>
  <td>
  <ul>
  <li>
  <p> Always break to None.</p>
  </li>
  <li>
  <p> No acknowledgment is required, the operation proceeds immediately.</p>
  </li>
  </ul>
  </td>
  </tr>
  </table>
  <p> </p>
  <h3><a id="FileRenameInformation__FileShortNameInformation__and_FileLinkInformation"></a><a id="filerenameinformation__fileshortnameinformation__and_filelinkinformation"></a><a id="FILERENAMEINFORMATION__FILESHORTNAMEINFORMATION__AND_FILELINKINFORMATION"></a>FileRenameInformation, FileShortNameInformation, and FileLinkInformation</h3>
  <p>This information applies when the following operations are being performed on a file or stream:</p>
  <ul>
  <li>
  <p> The file or stream is being renamed.</p>
  </li>
  <li>
  <p> A short name is being set for the file.</p>
  </li>
  <li>
  <p> A hard link is being created for the file. This affects oplock state if the new hard link is superseding an existing link to a different file, and the oplock exists on the link being superseded.</p>
  </li>
  <li>
  <p> An ancestor directory of the stream on which the oplock exists is being renamed, or the ancestor directory&#39;s short name is being set.</p>
  </li>
  </ul>
  <table>
  <tr>
  <th>Request Type</th>
  <th>Conditions</th>
  </tr>
  <tr>
  <td rowspan="2">
  <p>Batch</p>
  <p>Filter</p>
  </td>
  <td>
  <p>Broken on IRP_MJ_SET_INFORMATION (for FileRenameInformation, FileShortNameInformation, and FileLinkInformation) when:</p>
  <ul>
  <li>
  <p>  The operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td>
  <p> If the oplock is broken:</p>
  <ul>
  <li>
  <p>  Break to None.</p>
  </li>
  <li>
  <p> An acknowledgment must be received before the operation continues.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td rowspan="2">
  <p>Read-Handle</p>
  </td>
  <td>
  <p>Broken on IRP_MJ_SET_INFORMATION (for FileRenameInformation, FileShortNameInformation, and FileLinkInformation) when:</p>
  <ul>
  <li>
  <p>  The operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td>
  <p> If the oplock is broken:</p>
  <ul>
  <li>
  <p>  Break to Read.</p>
  </li>
  <li>
  <p> An acknowledgment must be received before the operation continues.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td rowspan="2">
  <p>Read-Write-Handle</p>
  </td>
  <td>
  <p>Broken on IRP_MJ_SET_INFORMATION (for FileRenameInformation, FileShortNameInformation, and FileLinkInformation) when:</p>
  <ul>
  <li>
  <p> The operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td>
  <p>If the oplock is broken:</p>
  <ul>
  <li>
  <p> Break to Read-Write.</p>
  </li>
  <li>
  <p> An acknowledgment must be received before the operation continues.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td>
  <p>Level 1</p>
  <p>Level 2</p>
  <p>Read</p>
  <p>Read-Write</p>
  </td>
  <td>
  <ul>
  <li>
  <p> The oplock is not broken, no acknowledgment is required, and the operation proceeds immediately.</p>
  </li>
  </ul>
  </td>
  </tr>
  </table>
  <p> </p>
  <h3><a id="FileDispositionInformation"></a><a id="filedispositioninformation"></a><a id="FILEDISPOSITIONINFORMATION"></a>FileDispositionInformation</h3>
  <p>This information applies when a caller tries to delete the file.</p>
  <table>
  <tr>
  <th>Request Type</th>
  <th>Conditions</th>
  </tr>
  <tr>
  <td rowspan="2">
  <p>Read-Handle</p>
  </td>
  <td>
  <p>Broken on IRP_MJ_SET_INFORMATION (for FileDispositionInformation) when:</p>
  <ul>
  <li>
  <p>The operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</p>
  <p><b>AND</b></p>
  </li>
  <li>
  <p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545765"><b>FILE_DISPOSITION_INFORMATION</b></a>.DeleteFile is <b>TRUE</b>.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td>
  <p>If the oplock is broken:</p>
  <ul>
  <li>
  <p> Break to Read.</p>
  </li>
  <li>
  <p>An acknowledgment must be received before the operation continues.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td rowspan="2">
  <p>Read-Write-Handle</p>
  </td>
  <td>
  <p>Broken on IRP_MJ_SET_INFORMATION (for FileDispositionInformation) when:</p>
  <ul>
  <li>
  <p>The operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT which owns the oplock.</p>
  <p><b>AND</b></p>
  </li>
  <li>
  <p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545765"><b>FILE_DISPOSITION_INFORMATION</b></a>.DeleteFile is <b>TRUE</b>.</p>
  </li>
  </ul>
  </td>
  </tr>
  <tr>
  <td>
  <p>If the oplock is broken:</p>
  <ul>
  <li>
  <p> Break to Read-Write.</p>
  </li>
  <li>
  <p>An acknowledgment must be received before the operation continues.</p>
  </li>
  </ul>
  </td>
  </tr>
  </table>
 




