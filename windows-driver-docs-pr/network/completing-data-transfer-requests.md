---
title: Completing Data Transfer Requests
description: Completing Data Transfer Requests
ms.assetid: 4c187202-c7a8-4fd8-984a-5bae647b74b0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Completing Data Transfer Requests





The Windows Sockets switch transfers data on a SAN socket asynchronously. Whenever the switch calls the SAN service provider's [**WSPSend**](https://msdn.microsoft.com/library/windows/hardware/ff566316), [**WSPRecv**](https://msdn.microsoft.com/library/windows/hardware/ff566309), [**WSPRdmaWrite**](https://msdn.microsoft.com/library/windows/hardware/ff566306), or [**WSPRdmaRead**](https://msdn.microsoft.com/library/windows/hardware/ff566304) data-transfer function, it specifies a pointer to an overlapped structure (WSAOVERLAPPED) and **NULL** for a completion routine. Even if the switch calls the SAN service provider's [**WSPEventSelect**](https://msdn.microsoft.com/library/windows/hardware/ff566287) function to indicate that the socket is in nonblocking mode, the SAN service provider is not required to implement nonblocking semantics for these data-transfer functions.

As described in the Windows Sockets API and SPI documentation in the Microsoft Windows SDK documentation, both blocking and nonblocking sockets treat overlapped operations the same. That is, the SAN service provider starts the particular data transfer operation and then immediately returns control to the switch. These data-transfer functions return error code WSA\_IO\_PENDING to indicate that an asynchronous operation started and that completion of that operation occurs later. After the operation completes, the SAN service provider signals completion if the switch requires completion notification as described in following paragraphs.

Because the switch always specifies **NULL** for a completion routine for overlapped data transfer operations, a SAN service provider is not required to support completion through the use of asynchronous procedure calls (APCs).

Whenever possible, the switch attempts to call the SAN service provider's [**WSPGetOverlappedResult**](https://msdn.microsoft.com/library/windows/hardware/ff566288) function to poll for completion of data transfer requests. In this way, the switch can avoid the overhead associated with active overlapped completion mechanisms. To indicate to a SAN service provider that the switch does not require completion notification for a particular overlapped data transfer operation, the switch sets the low-order bit of the **hEvent** member in the [**WSAOVERLAPPED**](https://msdn.microsoft.com/library/windows/hardware/ff565952) structure to one. The SAN service provider must not notify the switch of the completion of requests submitted in this manner.

If the switch requires notification of the completion of an overlapped data transfer operation, it sets the low-order bit of the **hEvent** member in the WSAOVERLAPPED structure to zero. The SAN service provider must complete data transfer operations that are initiated in this way by calling the **WPUCompleteOverlappedRequest** function to signal completion. In this call, the SAN service provider passes a pointer to the WSAOVERLAPPED structure that corresponds to a completed data transfer operation. In this **WPUCompleteOverlappedRequest** call, the SAN service provider also passes the socket descriptor that was acquired from the switch in a call to the **WPUCreateSocketHandle** function. The switch receives completion notifications, matches them to an application's I/O requests, and completes those I/O requests, as appropriate, for the application. For information about the **WPUCompleteOverlappedRequest** and **WPUCreateSocketHandle** functions, see the Windows SDK documentation.

 

 





