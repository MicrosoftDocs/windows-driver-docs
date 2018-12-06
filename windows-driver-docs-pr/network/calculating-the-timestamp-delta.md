---
title: Calculating the Timestamp Delta
description: Calculating the Timestamp Delta
ms.assetid: ed8daa7b-4804-4fef-9f63-fa06bc9e02ae
keywords:
- timestamps WDK TCP chimney offload , calculating delta
- TCP timestamps WDK TCP chimney offload , calculating delta
- calculating timestamp delta WDK TCP chimney offload
- delta calculation WDK TCP timestamps
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calculating the Timestamp Delta


\[The TCP chimney offload feature is deprecated and should not be used.\]

When the host stack offloads a TCP connection, it supplies the following timestamp-related variables in the TCP delegated state for the connection:

<a href="" id="tsrecent"></a>*TsRecent*  
The timestamp value to send in the next acknowledgement (Ts.Recent in RFC 1323)

<a href="" id="tsrecentage"></a>*TsRecentAge*  
The amount of time, in clock ticks, since the most recent timestamp was received (RFC 1323)

<a href="" id="tstime"></a>*TsTime*  
The current value of the adjusted time stamp

The offload target uses *TsRecent* and *TsRecentAge* in accordance with RFC 1323. The offload target uses *TsTime* to calculate its own timestamp delta.

*TsTime* specifies the current value of the host stack's timestamp value, which is equivalent to the host stack's current clock time plus the host's timestamp delta, if any:

*TsTime*= *StackTime*+ *StackDelta*

When a connection is initially offloaded, the timestamp delta is always zero.

The offload target subtracts its current time from the value of *TsTime* that is supplied by the host stack to arrive at the offload target's timestamp delta:

*NicDelta*= *TsTime*- *NicTime*

For example, if the host stack supplies 100 in the *TsTime* variable and if the offload target's current time is 200, the offload target subtracts 200 from 100 to get an offload target timestamp delta of -100.

Similarly, when the offload target terminates of the offload of a connection, it supplies a value in *TsTime* in the TCP delegated state for the connection. In this situation, the value of *TsTime* is the offload target's current time plus the offload target's timestamp delta. The host stack subtracts its current time from the value *TsTime* to arrive at the host stack timestamp delta.

 

 





