---
title: Debugger Data Model C++ Additional Interfaces
description: This topic describes  additional interfaces associated with the Debugger C++ Data Model, such as metadata, concepts and object enumeration.
ms.date: 09/12/2018
---

# Debugger Data Model C++ Additional Interfaces

This topic describes some additional interfaces associated with the Debugger C++ Data Model, such as metadata, concepts and object enumeration.

## <span id="metadatainterfaces"></span> Debugger Data Model Metadata Interfaces

One of the core notions in the data model is that an object (particularly a synthetic one) is a dictionary of key/value/metadata tuples. Each key can have an entire store of metadata associated with it that describes a variety of things surrounding the key and its potential value. Note that the metadata does not, in any way, change the value of the key. It is only ancillary information associated with the key and its value which may affect the presentation or other associated attributes of the key and its value. 

In some senses, a metadata store is not all that different from the key/value/metadata tuples that are the essence of an object in the data model. It is, however, simplified from this view. A metadata store is represented by the IKeyStore interface. While also a collection of key/value/metadata tuples, there are limitations to what can be done with a metadata key store versus a model object: 

- A key store can only have a single parent store -- it cannot have an arbitrary chain of parent models.
- A key store has no concepts. It can only have the dictionary of key/value/metadata tuples. This means that the keys present in a key store are static. They can not be created on demand by a dynamic language system.
- By convention only, the values in a metadata defined key store are restricted to basic values (intrinsics and property accessors)

While a key store can have an arbitrary number (and arbitrary naming) of keys, there are certain names that have defined semantic values. Presently, those names are: 

Key Name | Value Type | Description
|--------------|------------------|--------------|
PreferredRadix | Integer: 2, 8, 10, or 16 | Indicates what radix an ordinal value should be displayed in
PreferredFormat | Integer: as defined by the PreferredFormat enumeration | Indicates the preferred formatting type for display of the value
PreferredLength | Integer | For arrays and other containers, indicates how many elements should be displayed by default
FindDerivation | Boolean | Indicates whether the debug host should perform derived type analysis on the value before using (e.g.: displaying)
Help | String | Tool tip style help text for the key which can be presented by the user interface in an appropriately helpful way.
ActionName | String | Indicates that the given method (one which takes no arguments and returns no values) is an action. The name of the action is specified in metadata. A user interface may utilize this name to present the option in a context menu or other appropriate interface
ActionIsDefault | Boolean | Only valid if the ActionName key is specified, indicates that this is the default action for the object.
ActionDescription | String | Only valid if the ActionName key is specified, this gives a tool tip style description for the action. Such text can be presented by the user interface in an appropriately helpful way.

Note that while keys in the metadata store can have their own metadata (ad infiniteum), there is currently no use for such. Most callers will specify null for any metadata parameters in methods on the IKeyStore interface. 

**The Core Metadata Interface: IKeyStore**

The IKeyStore interface is defined as follows: 

```cpp
DECLARE_INTERFACE_(IKeyStore, IUnknown)
{
   STDMETHOD(GetKey)(_In_ PCWSTR key, _COM_Errorptr_opt_ IModelObject** object, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
   STDMETHOD(SetKey)(_In_ PCWSTR key, _In_opt_ IModelObject* object, _In_opt_ IKeyStore* metadata) PURE;
   STDMETHOD(GetKeyValue)(_In_ PCWSTR key, _COM_Errorptr_opt_ IModelObject** object, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
   STDMETHOD(SetKeyValue)(_In_ PCWSTR key, _In_ IModelObject* object) PURE;
   STDMETHOD(ClearKeys)() PURE;
}
```

[GetKey](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-ikeystore-getkey)

The GetKey method is analogous to the GetKey method on IModelObject. It will return the value of the specified key if it exists in the key store or the key store's parent store. Note that if the value of the key is a property accessor, the GetValue method will not be called on the property accessor. The actual IModelPropertyAccessor boxed into an IModelObject will be returned. It is typical that a client will call GetKeyValue for this reason. 

[SetKey](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-ikeystore-setkey)

The SetKey method is analogous to the SetKey method on IModelObject. It is the only method which is capable of creating a key and associating metadata with it within the key store. 

[GetKeyValue](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-ikeystore-getkeyvalue)

The GetKeyValue method is the first method a client will go to in order to find the value of a particular key within the metadata store. If the key specified by the key argument exists within the store (or it's parent store), the value of that key and any metadata associated with it will be returned. If the value of the key is a property accessor (an IModelPropertyAccessor boxed into an IModelObject), the GetValue method of the property accessor will automatically be called by GetKeyValue and the underlying value of the property returned. 

[SetKeyValue](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-ikeystore-setkeyvalue)

The SetKeyValue method is analogous to the SetKeyValue method on IModelObject. This method is not capable of creating a new key within the metadata store. If there is an existing key as indicated by the key argument, its value will be set as indicated. If the key is a property accessor, the SetValue method will be called on the property accessor in order to set the underlying value. Note that metadata is typically static once created. Use of this method on a metadata key store should be infrequent. 

[ClearKeys](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-ikeystore-clearkeys)

The ClearKeys method is analogous to the ClearKeys method on IModelObject. It will remove every key from the given metadata store. This method has no effect on any parent store. 


## <span id="object"></span> Object Enumeration in the Data Model

**Enumerating Objects in the Data Model**

There are two core key enumeration interfaces in the data model: IKeyEnumerator and IRawEnumerator. While these are the two core interfaces, they can be used to enumerate objects in one of three styles: 

*Keys* - The IKeyEnumerator interface can be acquired via a call to EnumerateKeys in order to enumerate the keys of an object and their values/metadata without resolving any underlying property accessors. This style of enumeration can return raw IModelPropertyAccessor values boxed into IModelObjects.

*Values* - The IKeyEnumerator and IRawEnumerator interfaces can be acquired via calls to either EnumerateKeyValues or EnumerateRawValues in order to enumerate the keys/raw values on an object and their values/metadata. Any property accessors present in the enumeration are automatically resolved via a call to the underlying GetValue method during such an enumeration.

*References* - The IKeyEnumerator and IRawEnumerator interfaces can be acquired via calls to either EnumerateKeyReferences or EnumerateRawReferences in order to enumerate references to the keys/raw values on an object. Such references can be saved and later used to get or set the underlying key or raw value.

**KeyEnumerator: Enumeration of synthetic keys**

The IKeyEnumerator interface is the single interface for the enumeration of all keys (by key, value, or reference) within an instance object and all the associated parent models in its parent model chain. The interface is defined as follows: 

```cpp
DECLARE_INTERFACE_(IKeyEnumerator, IUnknown)
{
    STDMETHOD(Reset)() PURE;
    STDMETHOD(GetNext)(_Out_ BSTR* key, _COM_Errorptr_opt_ IModelObject** value, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
}
```

[Reset](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-ikeyenumerator-reset)

The Reset method resets the enumerator to the position it was at when it was first acquired (e.g.: before the first element in the enumeration). A subsequent call to GetNext will return the first enumerated key. 

[GetNext](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-ikeyenumerator-getnext)

The GetNext method both moves the enumerator forward and returns the key at that position in the enumeration.


**IRawEnumerator: Enumeration of native or underlying language (C/C++) constructs**

The IRawEnumerator interface is the single interface for the enumeration of all native/language constructs (by value or reference) within a object which represents a native construct within the address space of the debug target. 
The interface is defined as follows: 

```cpp
DECLARE_INTERFACE_(IRawEnumerator, IUnknown)
{
    STDMETHOD(Reset)() PURE;
    STDMETHOD(GetNext)(_Out_opt_ BSTR* name, _Out_opt_ SymbolKind *kind, _COM_Errorptr_opt_ IModelObject** value) PURE;
}
```

[Reset](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-irawenumerator-reset)

The Reset method resets the enumerator to the position it was at when it was first acquired (e.g.: before the first element in the enumeration). A subsequent call to GetNext will return the first enumerated native/language construct. 

[GetNext](/windows-hardware/drivers/ddi/dbgmodel/nf-dbgmodel-irawenumerator-getnext)

The GetNext method both moves the enumerator forward and returns the native/language construct at that position in the enumeration. 

---

## <span id="related_topics"></span>See also

This topic is part of a series which describes the interfaces accessible from C++, how to use them to build a C++ based debugger extension, and how to make use of other data model constructs (e.g.: JavaScript or NatVis) from a C++ data model extension.

[Debugger Data Model C++ Overview](data-model-cpp-overview.md)

[Debugger Data Model C++ Interfaces](data-model-cpp-interfaces.md)

[Debugger Data Model C++ Objects](data-model-cpp-objects.md)

[Debugger Data Model C++ Additional Interfaces](data-model-cpp-additional-interfaces.md)

[Debugger Data Model C++ Concepts](data-model-cpp-concepts.md)

[Debugger Data Model C++ Scripting](data-model-cpp-scripting.md)