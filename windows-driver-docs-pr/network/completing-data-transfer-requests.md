---
title: Completing Data Transfer Requests
description: Completing Data Transfer Requests
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Completing Data Transfer Requests





The Windows Sockets switch transfers data on a SAN socket asynchronously. Whenever the switch calls the SAN service provider's [**WSPSend**](/previous-versions/windows/hardware/network/ff566316(v=vs.85)), [**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85)), [**WSPRdmaWrite**](/previous-versions/windows/hardware/network/ff566306(v=vs.85)), or [**WSPRdmaRead**](/previous-versions/windows/hardware/network/ff566304(v=vs.85)) data-transfer function, it specifies a pointer to an overlapped structure (WSAOVERLAPPED) and **NULL** for a completion routine. Even if the switch calls the SAN service provider's [**WSPEventSelect**](/previous-versions/windows/hardware/network/ff566287(v=vs.85)) function to indicate that the socket is in nonblocking mode, the SAN service provider is not required to implement nonblocking semantics for these data-transfer functions.

As described in the Windows Sockets API and SPI documentation in the Microsoft Windows SDK documentation, both blocking and nonblocking sockets treat overlapped operations the same. That is, the SAN service provider starts the particular data transfer operation and then immediately returns control to the switch. These data-transfer functions return error code WSA\_IO\_PENDING to indicate that an asynchronous operation started and that completion of that operation occurs later. After the operation completes, the SAN service provider signals completion if the switch requires completion notification as described in following paragraphs.

Because the switch always specifies **NULL** for a completion routine for overlapped data transfer operations, a SAN service provider is not required to support completion through the use of asynchronous procedure calls (APCs).

Whenever possible, the switch attempts to call the SAN service provider's [**WSPGetOverlappedResult**](/previous-versions/windows/hardware/network/ff566288(v=vs.85)) function to poll for completion of data transfer requests. In this way, the switch can avoid the overhead associated with active overlapped completion mechanisms. To indicate to a SAN service provider that the switch does not require completion notification for a particular overlapped data transfer operation, the switch sets the low-order bit of the **hEvent** member in the [**WSAOVERLAPPED**](/previous-versions/windows/hardware/network/ff565952(v=vs.85)) structure to one. The SAN service provider must not notify the switch of the completion of requests submitted in this manner.

If the switch requires notification of the completion of an overlapped data transfer operation, it sets the low-order bit of the **hEvent** member in the WSAOVERLAPPED structure to zero. The SAN service provider must complete data transfer operations that are initiated in this way by calling the **WPUCompleteOverlappedRequest** function to signal completion. In this call, the SAN service provider passes a pointer to the WSAOVERLAPPED structure that corresponds to a completed data transfer operation. In this **WPUCompleteOverlappedRequest** call, the SAN service provider also passes the socket descriptor that was acquired from the switch in a call to the **WPUCreateSocketHandle** function. The switch receives completion notifications, matches them to an application's I/O requests, and completes those I/O requests, as appropriate, for the application. For information about the **WPUCompleteOverlappedRequest** and **WPUCreateSocketHandle** functions, see the Windows SDK documentation.

 

