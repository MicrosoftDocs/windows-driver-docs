---
title: Sending Urgent Data on a SAN
description: Sending Urgent Data on a SAN
keywords:
- urgent data WDK SANs
ms.date: 04/20/2017
---

# Sending Urgent Data on a SAN





If an application sends urgent data on a SAN, the Windows Sockets switch transfers that data as described in the following sequence:

1.  For requests to send urgent data, the switch receives a **WSPSend** call in which the MSG\_OOB flag is set.

2.  The switch copies the urgent data to the payload portion of a control message buffer.

3.  The switch calls the appropriate SAN service provider's [**WSPSend**](/previous-versions/windows/hardware/network/ff566316(v=vs.85)) function to transmit the urgent data contained in the control message to the remote peer connection for a SAN socket. The SAN NIC in turn transmits the urgent data.

4.  The switch at the remote peer receives the transmitted data into receive buffers that it posted with the [**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85)) function.

5.  The switch at the remote peer copies the received data from the receive buffers to private storage.

6.  The switch at the remote peer calls **WSPRecv** to repost the receive buffers.

7.  The switch at the remote peer delivers the data to an application in accordance with standard Windows Sockets procedures.

 

