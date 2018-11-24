---
title: Common WSD Scan Service Operation Error Codes
description: This topic lists error codes that are common to all WSD Scan Service operations.
ms.assetid: 138c29ff-5b2f-4145-95b0-4a9e8489bb37
keywords: ["Common WSD Scan Service Operation Error Codes Imaging Devices"]
topic_type:
- apiref
api_name:
- Common WSD Scan Service Operation Error Codes
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Common WSD Scan Service Operation Error Codes


This topic lists error codes that are common to all WSD Scan Service operations. If an operation results in multiple errors, the Scan Service should return the most specific error.

-   **Wsa:ActionNotSupported**

    The WSD Scan Service returns this fault when a client requests an operation that the Scan Service does not support.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Fault property</th>
    <th>Definition</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>[Code]</p></td>
    <td><p>soap:Sender</p></td>
    </tr>
    <tr class="even">
    <td><p>[Subcode]</p></td>
    <td><p>wsa:ActionNotSupported</p></td>
    </tr>
    <tr class="odd">
    <td><p>[Reason]</p></td>
    <td><p>The [wsa:action] cannot be processed at the receiver.</p></td>
    </tr>
    <tr class="even">
    <td><p>[Detail]</p></td>
    <td><p><em>The invalid operation name</em></p></td>
    </tr>
    </tbody>
    </table>

     

-   **InvalidArgs**

    The WSD Scan Service returns this fault when a client sends an invalid argument as part of an operation. The invalid argument could be any of the following:

    -   There are not enough *in* arguments.
    -   There are too many *in* arguments.
    -   There are no *in* argument by that name.
    -   One or more *in* arguments are of the wrong data type.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Fault property</th>
    <th>Definition</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>[Code]</p></td>
    <td><p>soap:Sender</p></td>
    </tr>
    <tr class="even">
    <td><p>[Subcode]</p></td>
    <td><p>wscn:InvalidArgs</p></td>
    </tr>
    <tr class="odd">
    <td><p>[Reason]</p></td>
    <td><p>At least one input argument is invalid.</p></td>
    </tr>
    <tr class="even">
    <td><p>[Detail]</p></td>
    <td><p><em>The invalid argument</em></p></td>
    </tr>
    </tbody>
    </table>

     

-   **OperationFailed**

    The WSD Scan Service can return this fault when the current state of the Scan Service prevents invoking the specified operation.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Fault property</th>
    <th>Definition</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>[Code]</p></td>
    <td><p>soap:Receiver</p></td>
    </tr>
    <tr class="even">
    <td><p>[Subcode]</p></td>
    <td><p>wscn:OperationFailed</p></td>
    </tr>
    <tr class="odd">
    <td><p>[Reason]</p></td>
    <td><p>The service cannot perform the requested operation.</p></td>
    </tr>
    <tr class="even">
    <td><p>[Detail]</p></td>
    <td><p><em>None</em></p></td>
    </tr>
    </tbody>
    </table>

     

-   **ServerErrorTemporaryError**

    The WSD Scan Service returns this fault when the server experiences a temporary error while the scanner is processing the operation. The client can try the unmodified request again at some later point in time with the expectation that the temporary internal error condition might have been cleared. If there is a more specific error that is defined that applies to a temporary error, such as disk full, the Scan Service should return that error code.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Fault property</th>
    <th>Definition</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>[Code]</p></td>
    <td><p>soap:Receiver</p></td>
    </tr>
    <tr class="even">
    <td><p>[Subcode]</p></td>
    <td><p>wprt:ServerErrorTemporaryError</p></td>
    </tr>
    <tr class="odd">
    <td><p>[Reason]</p></td>
    <td><p>The service had an unexpected error.</p></td>
    </tr>
    <tr class="even">
    <td><p>[Detail]</p></td>
    <td><p><em>None</em></p></td>
    </tr>
    </tbody>
    </table>

     

-   **ServerErrorInternalError**

    The WSD Scan Service returns this fault when the scanner encounters an unexpected condition that prevents it from fulfilling the request. This error differs from **ServerErrorTemporaryError** in that it implies a more permanent type of internal error and resending the operation will return the same fault.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Fault property</th>
    <th>Definition</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>[Code]</p></td>
    <td><p>soap:Receiver</p></td>
    </tr>
    <tr class="even">
    <td><p>[Subcode]</p></td>
    <td><p>wscn:ServerErrorInternalError</p></td>
    </tr>
    <tr class="odd">
    <td><p>[Reason]</p></td>
    <td><p>The service had an unexpected error.</p></td>
    </tr>
    <tr class="even">
    <td><p>[Detail]</p></td>
    <td><p><em>None</em></p></td>
    </tr>
    </tbody>
    </table>

     

 

 





