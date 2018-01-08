---
title: Collection list serialization helpers
description: The collection list serialization helper functions are used by the v2 sensor drivers, for performing serialization-related operations on SENSOR\_COLLECTION\_LIST structures.
ms.assetid: 586FEDD7-6BA1-4E76-8E8D-E486F4711FAE
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Collection list serialization helpers


The collection list serialization helper functions are used by the v2 sensor drivers, for performing serialization-related operations on [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) structures.

The helper functions are used along with the sensor device driver software interface (DDSI). And because these helper functions are architecture-independent, it is safe to use them for data transfer across process boundaries. For example, it is safe to use these helper functions during a call to DeviceIoControl.

**SerializationBufferAllocate**

Usage by sensor DDSI

-   Allocates a serialization buffer, and returns a pointer to the buffer.

Comments

-   A successful buffer allocation is indicated by a STATUS\_OK value. Otherwise, the appropriate NTSTATUS error code is returned.

**SerializationBufferFree**

Usage by sensor DDSI

-   Frees a serialization buffer that is no longer needed.

Comments

-   None.

**CollectionsListGetSerializedSize**

Usage by sensor DDSI

-   Retrieves the size of the serialization buffer.

Comments

-   Buffer size is returned as a ULONG variable.

**CollectionsListSerializeToBuffer**

Usage by sensor DDSI

-   Writes the [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) information to the serialization buffer.

Comments

-   A successful write operation is indicated by a STATUS\_OK value. Otherwise, the appropriate NTSTATUS error code is returned.

**CollectionsListAllocateBufferAndSerialize**

Usage by sensor DDSI

-   Allocates a serialization buffer, and then writes the [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) information to the buffer.

Comments

-   If buffer allocation is successful, the collection list information is written to the buffer. Otherwise, the write operation is not performed and the appropriate NTSTATUS error code is returned.

-   A successful write operation is indicated by a STATUS\_OK value. Otherwise, the appropriate NTSTATUS error code is returned.

**CollectionsListDeserializeFromBuffer**

Usage by sensor DDSI

-   Reads [**SENSOR\_COLLECTION\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn957092) information from a source buffer.

Comments

-   A successful read operation is indicated by a STATUS\_OK value. Otherwise, the appropriate NTSTATUS error code is returned.

### <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

|                          |                        |
|--------------------------|------------------------|
| Minimum supported client | Windows 8.1            |
| Minimum supported server | Windows Server 2012 R2 |
| Header                   | Sensorsutils.h         |

 

## <span id="related_topics"></span>Related topics


[Marshalling helper functions](marshalling-helper-functions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Collection%20list%20serialization%20helpers%20%20RELEASE:%20%2811/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





