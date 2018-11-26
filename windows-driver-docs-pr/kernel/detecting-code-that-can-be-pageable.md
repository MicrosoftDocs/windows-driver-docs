---
title: Detecting Code That Can Be Pageable
description: Detecting Code That Can Be Pageable
ms.assetid: 5e8a021d-09c3-4e63-b5a8-7559c384ae3d
keywords: ["pageable drivers WDK kernel , code detection", "detecting pageable code"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Detecting Code That Can Be Pageable





To detect code that runs at IRQL &gt;= DISPATCH\_LEVEL, use the [**PAGED\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff558773) macro. In debug mode, this macro generates a message if the code runs at IRQL &gt;= DISPATCH\_LEVEL. Add the macro as the first statement in a routine to mark the whole routine as paged code, as the following example shows:

```cpp
NTSTATUS 
MyDriverXxx( 
    IN OUT PVOID ParseContext OPTIONAL, 
    OUT PHANDLE Handle 
    ) 
{ 
    NTSTATUS Status; 
 
    PAGED_CODE(); 
. 
. 
. 
} 
```

To make sure that you are doing this correctly, run the [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) against your finished driver with the **Force IRQL Checking** option enabled. This option causes the system to automatically page out all pageable code every time that the driver raises IRQL to DISPATCH\_LEVEL or above. Using the Driver Verifier, you can quickly find any driver bugs in this area. Otherwise, these bugs will typically be found only by customers and they can frequently be very hard for you to reproduce.

 

 




