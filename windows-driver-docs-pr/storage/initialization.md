---
title: Initialization
description: Initialization
ms.date: 04/20/2017
---

# Initialization


The LSI\_U3 Storport miniport driver's entry points are initialized in the DriverEntry routine. Other important initialization routines are LsiU3HWInitialize and LsiU3FindAdapter. In the latter, the driver's synchronization model is set to *StorSynchronizeFullDuplex*, which means the driver can receive new requests while it is completing previous requests. In other words, it may be simultaneously queuing up new requests from Storport while it is asynchronously completing previous requests.

 

 




