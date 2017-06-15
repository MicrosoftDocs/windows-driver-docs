---
title: KTM Objects
author: windows-driver-content
description: KTM Objects
MS-HAID:
- 'ktm\_dg\_4d6dc7a4-e261-4158-904e-ebc33ada61db.xml'
- 'kernel.ktm\_objects'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 927a417b-35f5-49b8-85f3-7e6b1f5c0225
keywords: ["Kernel Transaction Manager WDK , objects", "KTM WDK , objects", "objects WDK KTM"]
---

# KTM Objects


The Kernel Transaction Manager (KTM) defines the following four object types:

-   [Transaction manager objects](transaction-manager-objects.md), which KTM uses to maintain memory-resident information about a [*log stream*](transaction-processing-terms.md#ktm-term-log-stream) for a [*transaction processing system*](transaction-processing-terms.md#ktm-term-transaction-processing-system) (TPS).

-   [Resource manager objects](resource-manager-objects.md), which represent the [*resource managers*](transaction-processing-terms.md#ktm-term-resource-manager) within a TPS.

-   [Transaction objects](transaction-objects.md), which represent the transactions that [*transactional clients*](transaction-processing-terms.md#ktm-term-transactional-client) create.

-   [Enlistment objects](enlistment-objects.md), which represent [*enlistments*](transaction-processing-terms.md#ktm-term-enlistment) that provide connections between transactions and resource managers.

These four object types all have the following characteristics:

-   To create an object and obtain an object handle, [TPS components](understanding-tps-components.md) can call a *create* routine.

-   To obtain additional object handles to an existing object, TPS components can call an *open* routine.

-   To obtain information about an object, TPS components can call a *query* routine.

-   To close an object handle, TPS components call [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417).

KTM assigns an identifier GUID to each object. For transaction objects, this identifier GUID is also known as a *unit of work (UOW) identifier* that clients can specify. TPS components can use the identifier GUIDs to track objects. A TPS component that creates an object can pass the object's identifier GUID to another component so that the latter component can open a handle to the object.

Any TPS component that uses KTM can call [**ZwEnumerateTransactionObject**](https://msdn.microsoft.com/library/windows/hardware/ff566450) to enumerate KTM objects, but most components do not have to call this routine.

This section contains the following topics:

[Transaction Manager Objects](transaction-manager-objects.md)

[Resource Manager Objects](resource-manager-objects.md)

[Transaction Objects](transaction-objects.md)

[Enlistment Objects](enlistment-objects.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20KTM%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


