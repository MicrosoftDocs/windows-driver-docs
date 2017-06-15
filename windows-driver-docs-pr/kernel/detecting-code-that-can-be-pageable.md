---
title: Detecting Code That Can Be Pageable
author: windows-driver-content
description: Detecting Code That Can Be Pageable
MS-HAID:
- 'MemMgmt\_58d5786e-dda3-4740-8812-939be461731f.xml'
- 'kernel.detecting\_code\_that\_can\_be\_pageable'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5e8a021d-09c3-4e63-b5a8-7559c384ae3d
keywords: ["pageable drivers WDK kernel , code detection", "detecting pageable code"]
---

# Detecting Code That Can Be Pageable


## <a href="" id="ddk-detecting-code-that-can-be-pageable-kg"></a>


To detect code that runs at IRQL &gt;= DISPATCH\_LEVEL, use the [**PAGED\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff558773) macro. In debug mode, this macro generates a message if the code runs at IRQL &gt;= DISPATCH\_LEVEL. Add the macro as the first statement in a routine to mark the whole routine as paged code, as the following example shows:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Detecting%20Code%20That%20Can%20Be%20Pageable%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


