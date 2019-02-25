---
title: Closed Captioning Streams
description: Closed Captioning Streams
ms.assetid: ee6cfac6-c532-4e73-81b2-ee767d2d6a4d
keywords:
- closed captioning streams WDK DVD decoder
- group of pictures WDK DVD decoder
- GOP WDK DVD decoder
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Closed Captioning Streams





Support for closed captioning is required. The DVD decoder minidriver must provide closed captioning information for the Microsoft line 21 decoder filter. Implementations may not simply decode the closed captioning information inside the MPEG2 decoder and add it to the video stream. The DVD decoder minidriver must present the closed captioning pin as an output pin. After the stream is opened, the DVD decoder minidriver receives SRB\_READ\_DATA requests on the stream. The DVD decoder minidriver queues these requests until closed captioning data is available.

When a group of pictures (GOP) start code is processed in the video stream, the DVD decoder minidriver looks for user data (closed captioning information) and returns that information using one of the stream request blocks (SRBs) present on the closed captioning stream queue. All data discontinuity and format block changes should be propagated from the video pin to the closed captioning pin.

 

 




