---
title: Detecting Overruns and Underruns
description: Detecting Overruns and Underruns
ms.assetid: d7d282c8-adde-49fc-a20e-d633abd6dd3f
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Detecting Overruns and Underruns


## <span id="ddk_detecting_overruns_and_underruns_dtools"></span><span id="DDK_DETECTING_OVERRUNS_AND_UNDERRUNS_DTOOLS"></span>


You can use the **Verify Start** or **Verify End** option in GFlags to align allocations from the special pool so that they are best suited to detect overruns (accessing memory past the end of the allocation) or underruns (accessing memory that precedes the beginning of the allocation).

-   **Verify Start** enables underrun detection on allocations from the special pool. This causes a bug check when a program tries to access memory preceding its special pool memory allocation.

-   **Verify End** enables overrun detection on allocations from the special pool. This causes a bug check when a program tries to access memory beyond its special pool memory allocation. Because overruns are much more common, **Verify End** is the default.

In Windows Vista and later versions of Windows, this option is available on the **System Registry** and **Kernel Flags** tabs. In earlier versions of Windows, it is available only on the **System Registry** tab.

**To specify special pool alignment**

1.  Click the **System Registry** tab.

2.  Click **Verify Start** or **Verify End**.

3.  Click **Apply**.

    The following screen shot shows the Verify Start and Verify End settings on the System **Registry** tab.

    ![screen shot illustrating the verify start and verify end options on the system registry tab](images/gflags-overruns.png)

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **Verify Start** and **Verify End** alignment settings apply to all allocations from the special pool, including special pool allocation requests set in Driver Verifier. If you set the alignment without specifying a pool tag or allocation size, then the settings apply only to requests set in Driver Verifier.

 

 





