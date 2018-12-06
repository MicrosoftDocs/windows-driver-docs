---
title: Sharing Transport Addresses
description: Sharing Transport Addresses
ms.assetid: 1f5bc91a-75eb-466c-ad7d-cfbe0e83dc17
keywords:
- sharing transport addresses
- binding sockets WDK Winsock Kernel
- local transport address bindings WDK Winsock Kernel
- transport addresses WDK Winsock Kernel
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sharing Transport Addresses


In most situations, a Winsock Kernel (WSK) application cannot bind a socket to a local transport address that is already in use by another socket. WSK applications can use the [SO\_EXCLUSIVEADDRUSE](https://msdn.microsoft.com/library/windows/hardware/ff570830) and [SO\_REUSEADDR](https://msdn.microsoft.com/library/windows/hardware/ff570833) socket options to control the sharing of the local transport address to which a socket is bound. Neither of these socket options are set for a socket by default. For more information about setting socket options, see [Performing Control Operations on a Socket](performing-control-operations-on-a-socket.md).

The following table shows the result of binding a second socket to a local transport address that is already in use by another socket. The *Wildcard* and *Specific* cases specify whether the socket is bound to a wildcard local transport address or to a specific local transport address.

 <table>
     <tr>
      <th colspan="2" rowspan="3">Second bind</th>
      <th colspan="6">First bind</th>
     </tr>
     <tr>
      <td colspan="2">
       <p>No socket options (default)
       </p>
      </td>
      <td colspan="2">
       <p>
        SO_REUSEADDR
       </p>
      </td>
      <td colspan="2">
       <p>
        SO_EXCLUSIVEADDRUSE
       </p>
      </td>
     </tr>
     <tr>
      <td>
       <p>
        Wildcard
       </p>
      </td>
      <td>
       <p>
        Specific
       </p>
      </td>
      <td>
       <p>
        Wildcard
       </p>
      </td>
      <td>
       <p>
        Specific
       </p>
      </td>
      <td>
       <p>
        Wildcard
       </p>
      </td>
      <td>
       <p>
        Specific
       </p>
      </td>
     </tr>
     <tr>
      <td rowspan="2">
       <p>
        No socket options (default)
       </p>
      </td>
      <td>
       <p>
        Wildcard
       </p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
      <td>
       <p>SUCCESS</p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
      <td>
       <p>SUCCESS</p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
      <td>
       <p>SUCCESS</p>
      </td>
     </tr>
     <tr>
      <td>
       <p>
        Specific
       </p>
      </td>
      <td>
       <p>CHECK</p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
      <td>
       <p>CHECK</p>
      </td>
      <td>
       <p>DENIED</p>
      </td>
      <td>
       <p>DENIED</p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
     </tr>
     <tr>
      <td rowspan="2">
       <p>
        SO_REUSEADDR
       </p>
      </td>
      <td>
       <p>
        Wildcard
       </p>
      </td>
      <td>
       <p>DENIED</p>
      </td>
      <td>
       <p>SUCCESS</p>
      </td>
      <td>
       <p>SUCCESS</p>
      </td>
      <td>
       <p>SUCCESS</p>
      </td>
      <td>
       <p>DENIED</p>
      </td>
      <td>
       <p>SUCCESS</p>
      </td>
     </tr>
     <tr>
      <td>
       <p>
        Specific
       </p>
      </td>
      <td>
       <p>CHECK</p>
      </td>
      <td>
       <p>DENIED</p>
      </td>
      <td>
       <p>SUCCESS</p>
      </td>
      <td>
       <p>SUCCESS</p>
      </td>
      <td>
       <p>DENIED</p>
      </td>
      <td>
       <p>DENIED</p>
      </td>
     </tr>
     <tr>
      <td rowspan="2">
       <p>
        SO_EXCLUSIVEADDRUSE
       </p>
      </td>
      <td>
       <p>
        Wildcard
       </p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
     </tr>
     <tr>
      <td>
       <p>
        Specific
       </p>
      </td>
      <td>
       <p>CHECK</p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
      <td>
       <p>CHECK</p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
       <td>
       <p>DENIED</p>
      </td>
      <td>
       <p>INUSE</p>
      </td>
     </tr>
    </table>    

The results are defined as follows:

<a href="" id="success"></a>SUCCESS  
The bind operation for the second socket succeeds. The WSK subsystem returns a status of STATUS\_SUCCESS.

<a href="" id="inuse"></a>INUSE  
The bind operation on the second socket fails. The WSK subsystem returns a status of STATUS\_ADDRESS\_ALREADY\_EXISTS.

<a href="" id="denied"></a>DENIED  
The bind operation on the second socket fails. The WSK subsystem returns a status of STATUS\_ACCESS\_DENIED.

<a href="" id="check"></a>CHECK  
An access check is performed to determine if the bind operation on the second socket succeeds or fails. If access is granted, the bind succeeds and the WSK subsystem returns a status of STATUS\_SUCCESS. If access is denied, the bind fails and the WSK subsystem returns a status of STATUS\_ACCESS\_DENIED.

In the cases defined in the previous table where an access check is performed, the second socket's security context is checked against the first socket's security descriptor.

-   A socket's security context is determined by the *OwningProcess* and *OwningThread* parameters that are passed to either the [WskSocket](https://msdn.microsoft.com/library/windows/hardware/ff571149) function or the [WskSocketConnect](https://msdn.microsoft.com/library/windows/hardware/ff571150) function when the socket is created. If no specific process or thread is specified when the socket is created, the security context of the process that created the socket is used.

-   A socket's security descriptor is specified by the *SecurityDescriptor* parameter that is passed to either the WskSocket function or the WskSocketConnect function when the socket is created. If no specific security descriptor is specified, the WSK subsystem uses a default security descriptor that does not permit sharing of transport addresses. A security descriptor can also be applied to a socket after the socket has been created by using the [SO\_WSK\_SECURITY](https://msdn.microsoft.com/library/windows/hardware/ff570835) socket option.

If the two sockets are bound to two different specific local transport addresses, there is no sharing of either transport address. In this situation the second bind operation will always complete successfully.

 

 





