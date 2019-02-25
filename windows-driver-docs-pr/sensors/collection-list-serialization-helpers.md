---
title: Collection list serialization helpers
description: The collection list serialization helper functions are used by the v2 sensor drivers, for performing serialization-related operations on SENSOR\_COLLECTION\_LIST structures.
ms.assetid: 586FEDD7-6BA1-4E76-8E8D-E486F4711FAE
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Collection list serialization helpers


The collection list serialization helper functions are used by the v2 sensor drivers, for performing serialization-related operations on [**SENSOR\_COLLECTION\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_collection_list) structures.

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

-   Writes the [**SENSOR\_COLLECTION\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_collection_list) information to the serialization buffer.

Comments

-   A successful write operation is indicated by a STATUS\_OK value. Otherwise, the appropriate NTSTATUS error code is returned.

**CollectionsListAllocateBufferAndSerialize**

Usage by sensor DDSI

-   Allocates a serialization buffer, and then writes the [**SENSOR\_COLLECTION\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_collection_list) information to the buffer.

Comments

-   If buffer allocation is successful, the collection list information is written to the buffer. Otherwise, the write operation is not performed and the appropriate NTSTATUS error code is returned.

-   A successful write operation is indicated by a STATUS\_OK value. Otherwise, the appropriate NTSTATUS error code is returned.

**CollectionsListDeserializeFromBuffer**

Usage by sensor DDSI

-   Reads [**SENSOR\_COLLECTION\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/sensorsdef/ns-sensorsdef-sensor_collection_list) information from a source buffer.

Comments

-   A successful read operation is indicated by a STATUS\_OK value. Otherwise, the appropriate NTSTATUS error code is returned.

## Requirements

|                          |                        |
|--------------------------|------------------------|
| Minimum supported client | Windows 8.1            |
| Minimum supported server | Windows Server 2012 R2 |
| Header                   | Sensorsutils.h         |

 

## Related topics


[Marshalling helper functions](marshalling-helper-functions.md)

 

 






