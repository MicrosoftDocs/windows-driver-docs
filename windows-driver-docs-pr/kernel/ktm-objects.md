---
title: KTM Objects
description: KTM Objects
ms.assetid: 927a417b-35f5-49b8-85f3-7e6b1f5c0225
keywords: ["Kernel Transaction Manager WDK , objects", "KTM WDK , objects", "objects WDK KTM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
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

 

 




