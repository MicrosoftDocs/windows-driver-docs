---
title: Debugger Data Model C++ Interfaces 
description: This topic describes how to use Debugger Data Model C++ Interfaces to extend and customize the capabilities of the debugger.
ms.author: domars
ms.date: 10/08/2018
---

# Debugger Data Model C++ Interfaces 

This topic provides and overview of how to use Debugger Data Model C++ Interfaces to extend and customize the capabilities of the debugger.

This topic is part of a series which describes the interfaces accessible from C++, how to use them to build a C++ based
debugger extension, and how to make use of other data model constructs (e.g.: JavaScript or NatVis) from a C++ data model extension.

[Debugger Data Model C++ Overview](data-model-cpp-overview.md)

[Debugger Data Model C++ Interfaces](data-model-cpp-interfaces.md)

[Debugger Data Model C++ Objects](data-model-cpp-objects.md)

[Debugger Data Model C++ Additional Interfaces](data-model-cpp-additional-interfaces.md)

[Debugger Data Model C++ Concepts](data-model-cpp-concepts.md)

[Debugger Data Model C++ Scripting](data-model-cpp-scripting.md)

---

## Topic Sections

This topic includes the following sections.

[Debugger Data Model C++ Host Interfaces](#hostinterface)

[Accessing the Data Model](#accessdatamodel)

[Debugger Data Model System Interfaces](#systeminterfaces)

---

## <span id="hostinterface"></span> Debugger Data Model C++ Host Interfaces

**The Debugger Data Model Host**

The Debugger Data Model is designed to be a componentized system which can be hosted in a variety of different contexts. Normally, the Data Model is hosted in the context of a debugger application. In order to be a host of the data model, a number of interfaces need to be implemented to expose core aspects of the debugger: its targeting, its memory spaces, its evaluator, its symbolic and type system, etc... While these interfaces are implemented by any application wishing to host the data model, they are consumed by both the core data model as well as any extension which interoperates with the data model. 

The set of core interfaces are: 

Interface Name | Description
|--------------|---------------|
IDebugHost | The core interface to the debug host.
IDebugHostStatus  | An interface allowing a client to query for the status of the host.
IDebugHostContext  | An abstraction of a context within the host (e.g.: a particular target, a particular process, a particular address space, etc...)
IDebugHostErrorSink  | An interface implemented by callers to receive errors from certain portions of the host and data model
IDebugHostEvaluator / IDebugHostEvaluator2  | The debug host's expression evaluator.
IDebugHostExtensibility  | An interface for extending the capabilities of the host or portions of it (such as the expression evaluator).

The type system and symbolic interfaces are: 

InterfaceName | Description
|--------------|---------------|
IDebugHostSymbols | Core interface which provides access to and resolution of symbols
IDebugHostSymbol / IDebugHostSymbol2  | Represents a single symbol of any kind. The particular symbol is a derivation of this interface.
IDebugHostModule | Represents a module loaded within a process. This is a kind of symbol.
IDebugHostType / IDebugHostType2  | Represents a native/language type.
IDebugHostConstant  | Represents a constant within symbolic information (e.g.: a non-type template argument in C++)
IDebugHostField  | Represents a field within a structure or class.
IDebugHostData | Represents data within a module (were this within a structure or class it would be an IDebugHostField)
IDebugHostBaseClass | Represents a base class.
IDebugHostPublic  | Represents a symbol within the publics table of a PDB. This does not have type information associated with it. It is a name and address.
IDebugHostModuleSignature | Represents a module signature -- a definition which will match a set of modules by name and/or version
IDebugHostTypeSignature | Represents a type signature -- a definition which will match a set of types by module and/or name


**The Core Host Interface: IDebugHost**

The IDebugHost interface is the core interface of any data model host. It is defined as follows: 

```cpp
DECLARE_INTERFACE_(IDebugHost, IUnknown)
{
    STDMETHOD(GetHostDefinedInterface)(_COM_Outptr_ IUnknown** hostUnk) PURE;
    STDMETHOD(GetCurrentContext)(_COM_Outptr_ IDebugHostContext** context) PURE;
    STDMETHOD(GetDefaultMetadata)(_COM_Outptr_ IKeyStore** defaultMetadataStore) PURE;
}
```

[GetHostDefinedInterface](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughost-gethostdefinedinterface)

The GetHostDefinedInterface method returns the host's main private interface, if such exists for the given host. For Debugging Tools for Windows, the interface returned here is an IDebugClient (cast to IUnknown). 

[GetCurrentContext](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughost-getcurrentcontext)

The GetCurrentContext method returns an interface which represents the current state of the debugger host. The exact meaning of this is left up to the host, but it typically includes things such as the session, process, and address space that is active in the user interface of the debug host. The returned context object is largely opaque to the caller but it is an important object to pass between calls to the debug host. When a caller is, for instance, reading memory, it is important to know which process and address space that memory is being read from. That notion is encapsulated in the notion of the context object which is returned from this method. 

[GetDefaultMetadata](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughost-getdefaultmetadata)

The GetDefaultMetadata method returns a default metadata store that may be used for certain operations (e.g.: string conversion) when no explicit metadata has been passed. This allows the debug host to have some control over the way some data is presented. For example, the default metadata may include a PreferredRadix key, allowing the host to indicate whether ordinals should be displayed in decimal or hexadecimal if not otherwise specified. 

Note that property values on the default metadata store must be manually resolved and must pass the object for which the default metadata is being queried. The GetKey method should be used in lieu of GetKeyValue. 

**The Status Interface: IDebugHostStatus** 

The IDebugHostStatus interface allows a client of the data model or the debug host to inquire about certain aspects of the debug host's status. The interface is defined as follows: 

```cpp
DECLARE_INTERFACE_(IDebugHostStatus, IUnknown)
{
    STDMETHOD(PollUserInterrupt)(_Out_ bool* interruptRequested) PURE;
}
```

[PollUserInterrupt](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughoststatus-polluserinterrupt)

The PollUserInterrupt method is used to inquire whether the user of the debug host has requested an interruption of the current operation. A property accessor in the data model may, for instance, call into arbitrary code (e.g.: a JavaScript method). That code may take an arbitrary amount of time. In order to keep the debug host responsive, any such code which may take an arbitrary amount of time should check for an interrupt request via calling this method. If the interruptRequested value comes back as true, the caller should immediately abort and return a result of E_ABORT. 


**The Context Interface: IDebugHostContext**

Context is one of the most important aspects of the data model and the underlying debug host. When you hold an object, it is important to be able to know where an object came from -- what process is it in, what address space is it associated with. Knowing this information allows the correct interpretation of things like pointer values. 
An object of the type IDebugHostContext must be passed to many methods on the debug host. This interface can be acquired in a number of ways:

- By getting the current context of the debugger: calling the GetCurrentContext method of IDebugHost
- By getting the context of an object: calling the GetContext method of IModelObject
- By getting the context of a symbol: calling the GetContext method of IDebugHostSymbol

In addition, there are two values which have special meaning in the context of an IDebugHostContext interface which is either returned from or passed to a data model or debug host method: 

*nullptr*: an indication that there is no context. It is perfectly valid for some objects to have no context. The Debugger object in the root namespace of the data model does not refer to anything within a specific process or address space. It has no context.

*USE_CURRENT_HOST_CONTEXT*: a sentinel value indicating that one should use the current UI context of the debug host. This value will never be returned from the debug host. It may, however, be passed to any debug host method which takes an input IDebugHostContext in lieu of explicitly calling the GetCurrentContext method of IDebugHost. Note that explicitly passing USE_CURRENT_HOST_CONTEXT is often more performant than explicitly getting the current context. 

The contexts of a host context are largely opaque to the caller. The only operation that a caller outside the core debug host can do with a host context is to compare it to another host context. 

The IDebugHostContext interface is defined as follows: 

```cpp
DECLARE_INTERFACE_(IDebugHostContext, IUnknown)
{
    STDMETHOD(IsEqualTo)(_In_ IDebugHostContext *pContext, _Out_ bool *pIsEqual) PURE;
}
```

[IsEqualTo](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostcontext-isequalto)

The IsEqualTo method compares a host context to another host context. If the two contexts are equivalent, an indication of this is returned. Note that this comparison is not interface equivalence. This compares the underlying opaque contents of the context itself. 


**The Error Sink: IDebugHostErrorSink**

The IDebugHostErrorSink is a means by which a client can receive notifications of errors which occur during certain operations and route those errors where needed. The interface is defined as follows: 

```cpp
enum ErrorClass
{
    ErrorClassWarning,
    ErrorClassError
}
```

```cpp
DECLARE_INTERFACE_(IDebugHostErrorSink, IUnknown)
{
    STDMETHOD(ReportError)(_In_ ErrorClass errClass, _In_ HRESULT hrError, _In_ PCWSTR message) PURE;
}
```

[ReportError](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosterrorsink-reporterror)

The ReportError method is a callback on the error sink to notify it that an error has occurred and allow the sink to route the error to whatever UI or mechanism is appropriate. 


**The Host Evaluator: IDebugHostEvaluator / IDebugHostEvaluator2**

One of the most important pieces of functionality which the debug host provides to clients is access to its language based expression evaluator. The IDebugHostEvaluator and IDebugHostEvaluator2 interfaces are the means to access that functionality from the debug host. 

The interfaces are defined as follows: 

```cpp
DECLARE_INTERFACE_(IDebugHostEvaluator2, IDebugHostEvaluator)
{
    //
    // IDebugHostEvaluator:
    //
    STDMETHOD(EvaluateExpression)(_In_ IDebugHostContext* context, _In_ PCWSTR expression, _In_opt_ IModelObject* bindingContext, _COM_Errorptr_ IModelObject** result, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
    STDMETHOD(EvaluateExtendedExpression)(_In_ IDebugHostContext* context, _In_ PCWSTR expression, _In_opt_ IModelObject* bindingContext, _COM_Errorptr_ IModelObject** result, _COM_Outptr_opt_result_maybenull_ IKeyStore** metadata) PURE;
    //
    // IDebugHostEvaluator2:
    //
    STDMETHOD(AssignTo)(_In_ IModelObject* assignmentReference, _In_ IModelObject* assignmentValue, _COM_Errorptr_ IModelObject** assignmentResult, _COM_Outptr_opt_result_maybenull_ IKeyStore** assignmentMetadata) PURE;
}
```

[EvaluateExpression](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostevaluator-evaluateexpression)

The EvaluateExpression method allows requests the debug host to evaluate a language (e.g.: C++) expression and return the resulting value of that expression evaluation boxed as an IModelObject. This particular variant of the method only allows language constructs. Any additional functionality which is presented within the expression evaluator of the debug host that is not present in the language (e.g.: LINQ query methods) is turned off for the evaluation. 

[EvaluateExtendedExpression](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostevaluator-evaluateextendedexpression)

The EvaluateExtendedExpression method is similar to the EvaluateExpression method except that it turns back on additional non-language functionality which a particular debug host chooses to add to its expression evaluator. For Debugging Tools for Windows, for example, this enables anonymous types, LINQ queries, module qualifiers, format specifiers, and other non-C/C++ functionality. 


**IDebugHostEvaluator2**

[AssignTo](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostevaluator2-assignto)

The AssignTo method performs assignment according to the semantics of the language being debugged. 


**The Host Extensibility Interface: IDebugHostExtensibility**

Certain functionality of the debug host is optionally subject to extensibility. This may, for instance, include the expression evaluator. The IDebugHostExtensibility interface is the means by which these extensibility points are accessed. 
The interface is defined as follows: 

```cpp
DECLARE_INTERFACE_(IDebugHostExtensibility, IUnknown)
{
    STDMETHOD(CreateFunctionAlias)(_In_ PCWSTR aliasName, _In_ IModelObject *functionObject) PURE;
    STDMETHOD(DestroyFunctionAlias)(_In_ PCWSTR aliasName) PURE;
}
```

[CreateFunctionAlias](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostextensibility-createfunctionalias)

The CreateFunctionAlias method creates a "function alias", a "quick alias" for a method implemented in some extension. The meaning of this alias is host specific. It may extend the host's expression evaluator with the function or it may do something entirely different. 

[DestroyFunctionAlias](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostextensibility-destroyfunctionalias)

The DestroyFunctionAlias method undoes a prior call to the CreateFunctionAlias method. The function will no longer be available under the quick alias name. 



## <span id="accessdatamodel"> Accessing the Data Model

First and foremost, the data model extensibility APIs are designed to be neutral to the application (typically a debugger) which acts as a host of the data model. In theory, any application can host the data model by providing a set of host APIs that expose the type system of the application's debug target(s) and a set of projected objects into the namespace of the data model about what targets, processes, threads, etc... are in those debug target(s). 

While the data model APIs -- those that begin IDataModel<em>, IDebugHost</em>, and the offshoots of IModelObject -- are designed to be portable, they do not define what a "debugger extension" is. Today, a component that wishes to extend Debugging Tools for Windows and the engine it provides must write an engine extension in order to get access to the data model. That engine extension needs only to be an engine extension in so much as that is the loading and bootstrapping mechanism for the extension. As such, a minimal implementation would provide: 

- **DebugExtensionInitialize**: A method which utilizes a created IDebugClient to get access to the data model and sets up object model manipulations.
- **DebugExtensionUninitialize**: A method which undoes the object model manipulations which were performed in DebugExtensionInitialize.
- **DebugExtensionCanUnload**: A method which returns whether the extension can unload. If there are still live COM objects in the extension, it must indicate this. This is the debugger's equivalent of COM's DllCanUnloadNow. If this returns the S_FALSE indication of inability to unload, the debugger can query this later to see if an unload is safe or it may reinitialize the extension by calling DebugExtensionInitialize again. The extension must be prepared to handle both paths.
- **DebugExtensionUnload**: A method which does any final cleanup required right before the DLL unloads

*The Bridge Interface: IHostDataModelAccess*

As mentioned, when DebugExtensionInitialize is called, it creates a debug client and gets access to the data model. Such access is provided by a bridge interface between the legacy IDebug* interfaces of Debugging Tools for Windows and the data model. This bridge interface is 'IHostDataModelAccess and is defined as follows: 

```cpp
DECLARE_INTERFACE_(IHostDataModelAccess, IUnknown)
{
   STDMETHOD(GetDataModel)(_COM_Outptr_ IDataModelManager** manager, _COM_Outptr_ IDebugHost** host) PURE;
}
```

[GetDataModel](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-ihostdatamodelaccess-getdatamodel)

The GetDataModel method is the method on the bridge interface which provides access to both sides of the data model: 
The debug host (the lower edge of the debugger) is expressed by the returned IDebugHost interface
The data model's main component -- the data model manager is expressed by the returned IDataModelManager interface



## <span id="systeminterfaces"></span> Debugger Data Model System Interfaces

**The Data Model Host**

The Debugger Data Model is designed to be a componentized system which can be hosted in a variety of different contexts. Normally, the Data Model is hosted in the context of a debugger application. In order to be a host of the data model, a number of interfaces need to be implemented to expose core aspects of the debugger: its targeting, its memory spaces, its evaluator, its symbolic and type system, etc... While these interfaces are implemented by any application wishing to host the data model, they are consumed by both the core data model as well as any extension which interoperates with the data model. 

The type system and symbolic interfaces are: 


Interface Name | Description
|--------------|------------------|
IDebugHostSymbols  | Core interface which provides access to and resolution of symbols
IDebugHostSymbol / IDebugHostSymbol2  | Represents a single symbol of any kind. The particular symbol is a derivation of this interface.
IDebugHostModule  | Represents a module loaded within a process. This is a kind of symbol.
IDebugHostType / IDebugHostType2  | Represents a native/language type.
IDebugHostConstant  | Represents a constant within symbolic information (e.g.: a non-type template argument in C++)
IDebugHostField | Represents a field within a structure or class.
IDebugHostData | Represents data within a module (were this within a structure or class it would be an IDebugHostField)
IDebugHostBaseClass  | Represents a base class.
IDebugHostPublic | Represents a symbol within the publics table of a PDB. This does not have type information associated with it. It is a name and address.
IDebugHostModuleSignature | Represents a module signature -- a definition which will match a set of modules by name and/or version
IDebugHostTypeSignature | Represents a type signature -- a definition which will match a set of types by module and/or name

The other core interfaces are: 

Interface Name | Description
|--------------|------------------|
IDebugHost | The core interface to the debug host.
IDebugHostStatus | An interface allowing a client to query for the status of the host.
IDebugHostContext | An abstraction of a context within the host (e.g.: a particular target, a particular process, a particular address space, etc...)
IDebugHostErrorSink | An interface implemented by callers to receive errors from certain portions of the host and data model
IDebugHostEvaluator / IDebugHostEvaluator2 | The debug host's expression evaluator.
IDebugHostExtensibility | An interface for extending the capabilities of the host or portions of it (such as the expression evaluator).


**The Main Symbolic Interface: IDebugHostSymbols**

The IDebugHostSymbols interface is the main starting point to access symbols in the debug target. This interface can be queried from an instance of IDebugHost and is defined as follows: 

```cpp
DECLARE_INTERFACE_(IDebugHostSymbols, IUnknown)
{
    STDMETHOD(CreateModuleSignature)(_In_z_ PCWSTR pwszModuleName, _In_opt_z_ PCWSTR pwszMinVersion, _In_opt_z_ PCWSTR pwszMaxVersion, _Out_ IDebugHostModuleSignature** ppModuleSignature) PURE;
    STDMETHOD(CreateTypeSignature)(_In_z_ PCWSTR signatureSpecification, _In_opt_ IDebugHostModule* module, _Out_ IDebugHostTypeSignature** typeSignature) PURE;
    STDMETHOD(CreateTypeSignatureForModuleRange)(_In_z_ PCWSTR signatureSpecification, _In_z_ PCWSTR moduleName, _In_opt_z_ PCWSTR minVersion, _In_opt_z_ PCWSTR maxVersion, _Out_ IDebugHostTypeSignature** typeSignature) PURE;
    STDMETHOD(EnumerateModules)(_In_ IDebugHostContext* context, _COM_Outptr_ IDebugHostSymbolEnumerator** moduleEnum) PURE;
    STDMETHOD(FindModuleByName)(_In_ IDebugHostContext* context, _In_z_ PCWSTR moduleName, _COM_Outptr_ IDebugHostModule **module) PURE;
    STDMETHOD(FindModuleByLocation)(_In_ IDebugHostContext* context, _In_ Location moduleLocation, _COM_Outptr_ IDebugHostModule **module) PURE;
    STDMETHOD(GetMostDerivedObject)(_In_opt_ IDebugHostContext *pContext, _In_ Location location, _In_ IDebugHostType* objectType, _Out_ Location* derivedLocation, _Out_ IDebugHostType** derivedType) PURE;
}
```

[CreateModuleSignature](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostsymbols-createmodulesignature)

The CreateModuleSignature method creates a signature which can be used to match a set of specific modules by name and optionally, by version. 
There are three components to a module signature: 

- A name: a matching module must have a name which is an exact case insensitive match against the name in the signature
- A minimum version: if specified, a matching module must have a minimum version which is at least as high as this version. Versions are specified in "A.B.C.D" format with each subsequent portion being less important than the prior. Only the first segment is mandatory.
- A maximum version: if specified, a matching module must have a maximum version which is no higher than this version. Versions are specified in "A.B.C.D" format with each subsequent portion being less important than the prior. Only the first segment is mandatory.

[CreateTypeSignature](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostsymbols-createtypesignature)

The CreateTypeSignature method creates a signature which can be used to match a set of concrete types by containing module and type name. The format of the type name signature string is specific to the language being debugged (and debug host). For C/C++, the signature string is equivalent to a NatVis Type Specification. That is, the signature string is a type name where wildcards (specified as *) are allowed for template arguments. 

[CreateTypeSignatureForModuleRange](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostsymbols-createtypesignatureformodulerange)

The CreateTypeSignatureForModuleRange method creates a signature which can be used to match a set of concrete types by module signature and type name. This is similar to the CreateTypeSignature method excepting that instead of passing a specific module to match for the signature, the caller passes the arguments necessary to create a module signature (as if the module signature were created with the CreateModuleSignature method). 

[EnumerateModules](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostsymbols-enumeratemodules)

The EnumerateModules method creates an enumerator which will enumerate every module available in a particular host context. That host context might encapsulate a process context or it might encapsulate something like the Windows kernel. 


[FindModuleByName](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostsymbols-findmodulebyname)

The FindModuleByName method will look through the given host context and locate a module which has the specified name and return an interface to it. It is legal to search for the module by name with or without the file extension. 

[FindModuleByLocation](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostsymbols-findmodulebylocation)

The FindModuleByLocation method will look through the given host context and determine what module contains the address given by the specified location. It will then return an interface to such module. 

[GetMostDerivedObject](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostsymbols-getmostderivedobject)

The GetMostDerivedObject will use the type system of the debugger to determine the runtime type of an object from its static type. This method will only use symbolic information and heuristics available at the type system layer in order to perform this analysis. Such information may include C++ RTTI (run time type information) or analysis of the shape of the virtual function tables of the object. It does not include things such as the preferred runtime type concept on an IModelObject. 
If the analysis cannot find a runtime type or cannot find a runtime type different from the static type passed into the method, the input location and type may be passed out. The method will not fail for these reasons. 



**The Core Individual Symbol Interface: IDebugHostSymbol**

Every symbol that can be returned from the data model host will derive in some fashion from IDebugHostSymbol. This is the core interface that every symbol implements regardless of the kind of symbol. Depending on the kind of symbol, a given symbol may implement a set of other interfaces which return attributes more unique to the particular kind of symbol represented by this interface. The IDebugHostSymbol2 / 
IDebugHostSymbol interface is defined as follows: 

```cpp
DECLARE_INTERFACE_(IDebugHostSymbol2, IDebugHostSymbol)
{
    // 
    // IDebugHostSymbol:
    //
    STDMETHOD(GetContext)(_COM_Outptr_ IDebugHostContext** context) PURE;
    STDMETHOD(EnumerateChildren)(_In_ SymbolKind kind, _In_opt_z_ PCWSTR name, _Out_ IDebugHostSymbolEnumerator **ppEnum) PURE;
    STDMETHOD(GetSymbolKind)(_Out_ SymbolKind *kind) PURE;
    STDMETHOD(GetName)(_Out_ BSTR* symbolName) PURE;
    STDMETHOD(GetType)(_Out_ IDebugHostType** type) PURE;
    STDMETHOD(GetContainingModule)(_Out_ IDebugHostModule **containingModule) PURE;
    STDMETHOD(CompareAgainst)(_In_ IDebugHostSymbol *pComparisonSymbol, _In_ ULONG comparisonFlags, _Out_ bool *pMatches) PURE;
    //
    // IDebugHostSymbol2
    //
    STDMETHOD(EnumerateChildrenEx)(_In_ SymbolKind kind, _In_opt_z_ PCWSTR name, _In_opt_ SymbolSearchInfo* searchInfo, _Out_ IDebugHostSymbolEnumerator **ppEnum) PURE;
}
```

It is very important to note that this interface represents many kinds of symbols -- delineated by the SymbolKind enumeration which has values as follows: 

Enumarant | Meaning
|--------------|------------------|
Symbol  | Unspecified symbol type 
SymbolModule | The symbol is a module and can be queried for IDebugHostModule
SymbolType | The symbol is a type and can be queried for IDebugHostType
SymbolField | The symbol is a field (a data member within a structure or class) and can be queried for IDebugHostField
SymbolConstant | The symbol is a constant value and can be queried for IDebugHostConstant
SymbolData | The symbol is data which is not a member of a structure or class and is queryable for IDebugHostData
SymbolBaseClass | The symbol is a base class and is queryable for IDebugHostBaseClass
SymbolPublic | The symbol is an entry in a module's publics table (having no type information) and is queryable for IDebugHostPublic
SymbolFunction | The symbol is a function and is queryable for IDebugHostData

[GetContext](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostsymbol-getcontext)

The GetContext method returns the context where the symbol is valid. While this will represent things such as the debug target and process/address space in which the symbol exists, it may not be as specific as a context retrieved from other means (e.g.: from an *IModelObject*). 

[EnumerateChildren](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostsymbol-enumeratechildren)

The EnumerateChildren method returns an enumerator which will enumerate all children of a given symbol. For a C++ type, for example, the base classes, fields, member functions, and the like are all considered children of the type symbol. 


**The Module Interface: IDebugHostModule**

The debugger's notion of a module that is loaded within some address space is represented in two distinct ways in the data model: 
At the type system level via the IDebugHostModule interface. Here, a module is a symbol and core attributes of the module are interface method calls
Projected at the data model level via the Debugger.Models.Module data model. This is an extensible encapsulation of the type system IDebugHostModule representation of a module.

The IDebugHostModule interface is defined as follows (ignoring methods that are generic to IDebugHostSymbol): 

```cpp
DECLARE_INTERFACE_(IDebugHostModule, IDebugHostSymbol)
{
    //
    // IDebugHostModule:
    //
    STDMETHOD(GetImageName)(_In_ bool allowPath, _Out_ BSTR* imageName) PURE;
    STDMETHOD(GetBaseLocation)(_Out_ Location* moduleBaseLocation) PURE;
    STDMETHOD(GetVersion)(_Out_opt_ ULONG64* fileVersion, _Out_opt_ ULONG64* productVersion) PURE;
    STDMETHOD(FindTypeByName)(_In_z_ PCWSTR typeName, _Out_ IDebugHostType** type) PURE;
    STDMETHOD(FindSymbolByRVA)(_In_ ULONG64 rva, _Out_ IDebugHostSymbol** symbol) PURE;
    STDMETHOD(FindSymbolByName)(_In_z_ PCWSTR symbolName, _Out_ IDebugHostSymbol** symbol) PURE;
}
```

[GetImageName](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostmodule-getimagename)

The GetImageName method returns the image name of the module. Depending on the value of the allowPath argument, the returned image name may or may not include the full path to the image.

[GetBaseLocation](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostmodule-getbaselocation)

The GetBaseLocation method returns the base load address of the module as a location structure. The returned location structure for a module will typically refer to a virtual address.

[GetVersion](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostmodule-getversion)

The GetVersion method returns version information about the module (assuming that such information can successfully be read out of the headers). If a given version is requested (via a non-nullptr output pointer) and it cannot be read, an appropriate error code will be returned from the method call. 

[FindTypeByName](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostmodule-findtypebyname)

The FindTypeByName method finds a type defined within the module by the type name and returns a type symbol for it. This method may return a valid IDebugHostType which would never be returned via explicit recursion of children of the module. The debug host may allow creation of derivative types -- types not ever used within the module itself but derived from types that are. As an example, if the structure MyStruct is defined in the symbols of the module but the type MyStruct ** is never used, the FindTypeByName method may legitimately return a type symbol for MyStruct ** despite that type name never explicitly appearing in the symbols for the module. 

[FindSymbolByRVA](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostmodule-findsymbolbyrva)

The FindSymbolByRVA method will find a single matching symbol at the given relative virtual address within the module. If there is not a single symbol at the supplied RVA (e.g.: there are multiple matches), an error will be returned by this method. Note that this method will prefer returning a private symbol over a symbol in the publics table. 

[FindSymbolByName](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostmodule-findsymbolbyname)

The FindSymbolByName method will find a single global symbol of the given name within the module. If there is not a single symbol matching the given name, an error will be returned by this method. Note that this method will prefer returning a private symbol over a symbol in the publics table. 


**Access to the Type System: IDebugHostType2 / IDebugHostType**

A given language/native type is described by the IDebugHostType2 or IDebugHostType interfaces. Note that some of the methods on these interfaces only apply for specific kinds of types. A given type symbol may refer to one of the following types as described by the TypeKind enumeration: 

Type Kind |  Description
|--------------|------------------|
TypeUDT | A user defined type (a struct, class, union, etc...). A model object which has a native type whose kind is TypeUDT has a canonical representation of ObjectTargetObject where the type is always kept inside the corresponding IModelObject.
TypePointer | A pointer. A model object which has a native type whose kind is TypePointer has a canonical representation of ObjectIntrinsic where the pointer's value is zero extended to VT_UI8 and kept as intrinsic data in this 64-bit form. Any type symbol of TypePointer has a base type (as returned by the GetBaseType method) of the type that the pointer points to.
TypeMemberPointer | A pointer to class member. A model object which has a native type whose kind is TypeMemberPointer has a canonical representation which is intrinsic (the value being the same as the pointer value). The exact meaning of this value is compiler/debug host specific.
TypeArray | An array. A model object which has a native type whose kind is TypeArray has a canonical representation of ObjectTargetObject. The base address of the array is the object's location (retrieved via the GetLocation method) and the type of the array is always kept. Any type symbol of TypeArray has a base type (as returned by the GetBaseType method) of the type that the array is an array of.
TypeFunction | A function.
TypeTypedef | A typedef. A model object which has a native type whose kind would otherwise be TypeTypedef has a canonical representation identical to the canonical representation of the final type underlying the typedef. This appears completely transparent to the end user of the object and the type information unless the explicit typedef methods of IDebugHostType2 are utilized to query typedef information or there is an explicit data model registered against the typedef. Note that the GetTypeKind method will never return TypeTypedef. Every method will return what the final type underlying the typedef would return. There are typedef specific methods on IDebugHostType2 which can be used to get the typedef specific information.
TypeEnum | An enum. A model object which has a native type whose kind is TypeEnum has a canonical representation of ObjectIntrinsic where the value and type of the intrinsic is identical to the enum value. 
TypeIntrinsic | An intrinsic (base type). A model object which has a native type whose kind is TypeIntrinsic has a canonical representation of ObjectIntrinsic. The type information may or may not be kept -- particularly if the underlying type is fully described by the variant data type (VT_*) of the intrinsic data stored in the IModelObject

The overall IDebugHostType2 / IDebugHostType interface is defined as follows (excluding IDebugHostSymbol methods): 

```cpp
DECLARE_INTERFACE_(IDebugHostType2, IDebugHostType)
{
    //
    // IDebugHostType:
    //
    STDMETHOD(GetTypeKind)(_Out_ TypeKind *kind) PURE;
    STDMETHOD(GetSize)(_Out_ ULONG64* size) PURE;
    STDMETHOD(GetBaseType)(_Out_ IDebugHostType** baseType) PURE;
    STDMETHOD(GetHashCode)(_Out_ ULONG* hashCode) PURE;
    STDMETHOD(GetIntrinsicType)(_Out_opt_ IntrinsicKind *intrinsicKind, _Out_opt_ VARTYPE *carrierType) PURE;
    STDMETHOD(GetBitField)(_Out_ ULONG* lsbOfField, _Out_ ULONG* lengthOfField) PURE;
    STDMETHOD(GetPointerKind)(_Out_ PointerKind* pointerKind) PURE;
    STDMETHOD(GetMemberType)(_Out_ IDebugHostType** memberType) PURE;
    STDMETHOD(CreatePointerTo)(_In_ PointerKind kind, _COM_Outptr_ IDebugHostType** newType) PURE;
    STDMETHOD(GetArrayDimensionality)(_Out_ ULONG64* arrayDimensionality) PURE;
    STDMETHOD(GetArrayDimensions)(_In_ ULONG64 dimensions, _Out_writes_(dimensions) ArrayDimension *pDimensions) PURE;
    STDMETHOD(CreateArrayOf)(_In_ ULONG64 dimensions, _In_reads_(dimensions) ArrayDimension *pDimensions, _COM_Outptr_ IDebugHostType** newType) PURE;
    STDMETHOD(GetFunctionCallingConvention)(_Out_ CallingConventionKind* conventionKind) PURE;
    STDMETHOD(GetFunctionReturnType)(_COM_Outptr_ IDebugHostType** returnType) PURE;
    STDMETHOD(GetFunctionParameterTypeCount)(_Out_ ULONG64* count) PURE;
    STDMETHOD(GetFunctionParameterTypeAt)(_In_ ULONG64 i, _Out_ IDebugHostType** parameterType) PURE;
    STDMETHOD(IsGeneric)(_Out_ bool* isGeneric) PURE;
    STDMETHOD(GetGenericArgumentCount)(_Out_ ULONG64* argCount) PURE;
    STDMETHOD(GetGenericArgumentAt)(_In_ ULONG64 i, _Out_ IDebugHostSymbol** argument) PURE;
    //
    // IDebugHostType2:
    //
    STDMETHOD(IsTypedef)(_Out_ bool* isTypedef) PURE;
    STDMETHOD(GetTypedefBaseType)(_Out_ IDebugHostType2** baseType) PURE;
    STDMETHOD(GetTypedefFinalBaseType)(_Out_ IDebugHostType2** finalBaseType) PURE;
    STDMETHOD(GetFunctionVarArgsKind)(_Out_ VarArgsKind* varArgsKind) PURE;
}
```

**IDebugHostType2/IDebugHostType General Methods**

The following IDebugHostType methods are general to any type regardless of what kind is returned from the GetTypeKind method: 

```cpp
STDMETHOD(GetTypeKind)(_Out_ TypeKind *kind) PURE;
STDMETHOD(GetSize)(_Out_ ULONG64* size) PURE;
STDMETHOD(GetBaseType)(_Out_ IDebugHostType** baseType) PURE;
STDMETHOD(GetHashCode)(_Out_ ULONG* hashCode) PURE;
```

[GetTypeKind](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-gettypekind)

The GetTypeKind method returns what kind of type (pointer, array, intrinsic, etc...) the symbol refers to. 

[GetSize](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-getsize)

The GetSize method returns the size of the type (as if one had done sizeof(type) in C++). 

[GetBaseType](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-getbasetype)

If the type is a derivative of another single type (e.g.: as MyStruct * is derived from MyStruct'), the GetBaseType method returns the base type of the derivation. For pointers, this returns the type pointed to. For arrays, this returns what the array is an array of. If the type is not such a derivative type, an error is returned. 

[GetHashCode](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-gethashcode)

The GetHashCode method returns a 32-bit hash code for the type. With the exception of a global match (e.g.: a type signature equivalent to * which matches everything if permitted by the host), any type instance which can match a particular type signature must return the same hash code. 
This method is used in conjunction with type signatures in order to match type signatures to type instances. 


**IDebugHostType2/IDebugHostType Intrinsic Methods**

The following IDebugHostType methods are specific to intrinsic types (or types which hold intrinsic data such as enums): 

```cpp
STDMETHOD(GetIntrinsicType)(_Out_opt_ IntrinsicKind *intrinsicKind, _Out_opt_ VARTYPE *carrierType) PURE;
```

[GetIntrinsicType](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-getintrinsictype)

The GetIntrinsicType method returns information about what kind of intrinsic the type is. Two values are returned out of this method: 

- The intrinsic kind indicates the overall type (e.g.: integer, unsigned, floating point) but not the size of the type (e.g.: 8 bit, 16 bit, 32 bit, 64 bit)
- The carrier type indicates how the intrinsic kind packs into a VARIANT structure. This is a VT_* constant.

The combination of the two values provides the full set of information about the intrinsic. 


**IDebugHostType2/IDebugHostType Bitfield Methods**

The following IDebugHostType methods are specific to types which store data in bitfields. Information about bitfield placement within an intrinsic is stored as part of the type symbol in the data model rather than being an attribute of the location. 

```cpp
STDMETHOD(GetBitField)(_Out_ ULONG* lsbOfField, _Out_ ULONG* lengthOfField) PURE;
```

[GetBitField](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-getbitfield)

If a given member of a data structure is a bitfield (e.g.: ULONG MyBits:8), the type information for the field carries with it information about the bitfield placement. The GetBitField method can be used to retrieve that information. This method will fail on any type which is not a bitfield. This is the only reason the method will fail. Simply calling this method and looking at success/failure is sufficient to distinguish a bit field from a non-bit field. 
If a given type does happen to be a bitfield, the field positions are defined by the half open set *(lsbOfField + lengthOfField : lsbOfField]*


**IDebugHostType2/IDebugHostType Pointer Related Methods**

The following IDebugHostType methods are specific to pointer types. Such are types where GetTypeKind returns TypePointer or TypeMemberPointer': 

```cpp
STDMETHOD(GetPointerKind)(_Out_ PointerKind* pointerKind) PURE;
STDMETHOD(GetMemberType)(_Out_ IDebugHostType** memberType) PURE;
```
[GetPointerKind](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-getpointerkind)

For types which are pointers, the GetPointerKind method returns the kind of pointer. This is defined by the PointerKind enumeration.

[GetMemberType](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-getmembertype)

For types which are pointer-to-member (as indicated by a type kind of TypeMemberPointer), the GetMemberType method returns the class the pointer is a pointer-to-member of. 


**IDebugHostType2/IDebugHostType Array Related Methods**

Arrays are types where GetTypeKind returns TypeArray. Note that arrays as defined by the debug host's type system are not the same as the single dimensional, zero index based, packed linear one dimensional arrays that C utilizes. C style arrays fit into the definition but the overall scope of an array is broader in IDebugHostType. 
An array in the debug host can be multi-dimensional and each dimension within the array is defined by a descriptor known as an ArrayDimensionThis descriptor has the following fields: 



Field | Meaning
|--------------|------------------|
LowerBound | The base index of the array as a signed 64-bit value. For a C style array, this will always be zero. It need not be. An individual dimension of an array can be considered to start at any 64-bit index, even a negative one.
Length | The length of the array dimension as an unsigned 64-bit value. The indicies of the array span the half open set [LowerBound, LowerBound + Length).
Stride | Defines the stride of the array dimension. For an increase of one (from N to N + 1) in the index of this dimension, this indicates how many bytes to move forward in memory. For a C style array, this would be the size of each element of the array. It does not need to be. Padding between elements can be expressed as a stride greater than the size of each individual element. For multi-dimensional arrays, this value would indicate how to move an entire dimension forward. Consider an M x N matrix. This might be described in row-major form as two dimensions: 

```cpp   
{ [LowerBound: 0, Length: M, Stride: N \* sizeof(element)], [LowerBound: 0, Length: N, Stride: sizeof(element)]} 
```
or it might be alternatively be described in column-major form as two dimensions: 

```cpp   
{ [LowerBound: 0, Length: M, Stride: sizeof(element)], [LowerBound: 0, Length: N, Stride: M \* sizeof(element)]} 
```
The ArrayDimension concept allows this degree of flexibility. 

The following IDebugHostType methods are specific to array types. 

```cpp
STDMETHOD(GetArrayDimensionality)(\_Out_ ULONG64\* arrayDimensionality) PURE; 
STDMETHOD(GetArrayDimensions)(\_In_ ULONG64 dimensions, \_Out_writes_(dimensions) ArrayDimension \*pDimensions) PURE;
```

[GetArrayDimensionality](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-getarraydimensionality)

The GetArrayDimensionality method returns the number of dimensions that the array is indexed in. For C style arrays, the value returned here will always be 1. 

[GetArrayDimensions](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-getarraydimensions)

The GetArrayDimensions method returns a set of descriptors, one for each dimension of the array as indicated by the GetArrayDimensionality method. Each descriptor is an ArrayDimension structure which describes the starting index, length, and forward stride of each array dimension. This allows descriptions of significantly more powerful array constructs than are allowed in the C type system. 

For C-style arrays, a single array dimension is returned here with values which are always: 

- LowerBound = 0
- Length = ARRAYSIZE(array)
- Stride = sizeof(elementType)


**IDebugHostType2/IDebugHostType Function Related Methods**

Types which indicate that they are function types via a kind of TypeFunction support the following methods in both IDebugHostType and IDebugHostType2. 

```cpp
//
// IDebugHostType:
//
STDMETHOD(GetFunctionCallingConvention)(_Out_ CallingConventionKind* conventionKind) PURE;
STDMETHOD(GetFunctionReturnType)(_COM_Outptr_ IDebugHostType** returnType) PURE;
STDMETHOD(GetFunctionParameterTypeCount)(_Out_ ULONG64* count) PURE;
STDMETHOD(GetFunctionParameterTypeAt)(_In_ ULONG64 i, _Out_ IDebugHostType** parameterType) PURE;
//
// IDebugHostType2:
//
STDMETHOD(GetFunctionVarArgsKind)(_Out_ VarArgsKind* varArgsKind) PURE;
```

[GetFunctionCallingConvention](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-getfunctioncallingconvention)

The GetFunctionCallingConvention method returns the calling convention of the function. Such is returned as a member of the CallingConventionKind enumeration. 

[GetFunctionReturnType](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-getfunctionreturntype)

The GetFunctionReturnType method returns the return type of the function. 

[GetFunctionParameterTypeCount](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-getfunctionparametertypecount)

The GetFunctionParameterTypeCount method returns the number of arguments that the function takes. Note that the C/C++ ellipsis based variable argument marker is not considered in this count. The presence of such must be detected via the GetFunctionVarArgsKind method. This will only include arguments before the ellipsis. 

[GetFunctionParameterTypeAt](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype-getfunctionparametertypeat)

The GetFunctionParameterTypeAt method returns the type of the i-th argument to the function. 

The GetFunctionVarArgsKind method returns whether a given function utilizes a variable argument list, and if so, what style of variable arguments it utilizes. Such is defined by a member of the VarArgsKind enumeration defined as follows: 

 Enumerant | Meaning
|---------|---------|
VarArgsNone | The function does not take any variable arguments.
VarArgsCStyle | The function is a C-style varargs function (returnType(arg1, arg2, ...)). The number of arguments reported by the function does not include the ellipsis argument. Any variable argument passing occurs after the number of arguments returned by the GetFunctionParameterTypeCount method.


**IDebugHostType2 GetFunctionVarArgsKind**

The GetFunctionVarArgsKind method returns whether a given function utilizes a variable argument list, and if so, what style of variable arguments it utilizes. Such is defined by a member of the VarArgsKind enumeration defined as follows: 


**IDebugHostType2/IDebugHostType Typedef Related Methods**

Any type which is a typedef will behave as if the type is the final type underlying the typedef. This means that methods such as GetTypeKind will not indicate that the type is a typedef. Likewise, GetBaseType will not return the type the definition refers to. They will instead indicate behave as if they were called on the final definition underlying the typedef. As an example: 

```cpp
typedef MYSTRUCT *PMYSTRUCT;
typedef PMYSTRUCT PTRMYSTRUCT;
```

An IDebugHostType for 'either PMYSTRUCT or PTRMYSTRUCT will report the following information: 

- The GetTypeKind method will return TypePointer. The final underlying type MYSTRUCT * is indeed a pointer.
- The 'GetBaseType method will return a type for MYSTRUCT. The underlying type of MYSTRUCT * is MYSTRUCT.

The only difference here is how the typedef specific methods on IDebugHostType2 behave. Those methods are: 

```cpp
STDMETHOD(IsTypedef)(_Out_ bool* isTypedef) PURE;
STDMETHOD(GetTypedefBaseType)(_Out_ IDebugHostType2** baseType) PURE;
STDMETHOD(GetTypedefFinalBaseType)(_Out_ IDebugHostType2** finalBaseType) PURE;
```

In this example: 

- The IsTypedef method will return true for both PMYSTRUCT and PTRMYSTRUCT
- The GetTypedefBaseType method will return MYSTRUCT * for PMYSTRUCT and PMYSTRUCT for PTRMYSTRUCT
- The GetTypedefFinalBaseType method will return MYSTRUCT * for both types

[IsTypedef](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype2-istypedef)

The IsTypedef method is the only method capable of seeing whether a type is a typedef. The GetTypeKind method will behave as if called on the underlying type. 

[GetTypedefBaseType](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype2-gettypedefbasetype)

The GetTypedefBaseType method will return what the immediate definition of the typedef. In the examples described in the documentation: 

```cpp
typedef MYSTRUCT *PMYSTRUCT;
typedef PMYSTRUCT PTRMYSTRUCT;
```
this method will return MYSTRUCT * for PMYSTRUCT and PMYSTRUCT for PTRMYSTRUCT.


[GetTypedefFinalBaseType](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttype2-gettypedeffinalbasetype)

The GetTypedefFinalBaseType method will return the final type that the typedef is a definition for. If the typedef is a definition of another typedef, this will continue to follow the definition chain until it reaches a type which is not a typedef and that type will be returned. In the examples described in the documentation: 

```cpp
typedef MYSTRUCT *PMYSTRUCT;
typedef PMYSTRUCT PTRMYSTRUCT;
```

this method will return MYSTRUCT * when called on either PMYSTRUCT or PTRMYSTRUCT. 

**IDebugHostType2/IDebugHostType Type Creation Methods**

```cpp
STDMETHOD(CreatePointerTo)(_In_ PointerKind kind, _COM_Outptr_ IDebugHostType** newType) PURE;
STDMETHOD(CreateArrayOf)(_In_ ULONG64 dimensions, _In_reads_(dimensions) ArrayDimension *pDimensions, _COM_Outptr_ IDebugHostType** newType) PURE;
```

**Constant Symbol Values: IDebugHostConstant**

For locations where constant values are present in symbolic information (where a particular value is a symbol which may or may not be a constant value), the IDebugHostConstant interface expresses the notion of such a constant. This is typically used in places like template arguments where a given argument is typically a type but may instead be a non-type template argument (e.g.: a constant). 

The IDebugHostConstant interface is defined as follows (ignoring generic methods implemented by IDebugHostSymbol): 

```cpp
DECLARE_INTERFACE_(IDebugHostConstant, IDebugHostSymbol)
{
    STDMETHOD(GetValue)(_Out_ VARIANT* value) PURE;
}
```

[GetValue](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostconstant-getvalue)

The GetValue method returns the value of the constant packed into a VARIANT. It is important to note that the GetType method on IDebugHostSymbol may return a specific type symbol for the constant. In such cases, there is no guarantee that the packing of the constant value as defined by the type symbol is the same as the packing as returned by the GetValue method here. 


**Data Member Access: IDebugHostField**

The IDebugHostField class represents a symbol which is a data member of a class, structure, union, or other type construct. It does not represent free data (e.g.: global data). The interface is defined as follows (ignoring methods generic to IDebugHostSymbol): 

```cpp
DECLARE_INTERFACE_(IDebugHostField, IDebugHostSymbol)
{
    STDMETHOD(GetLocationKind)(_Out_ LocationKind *locationKind) PURE;
    STDMETHOD(GetOffset)(_Out_ ULONG64* offset) PURE;
    STDMETHOD(GetLocation)(_Out_ Location* location) PURE;
    STDMETHOD(GetValue)(_Out_ VARIANT* value) PURE;
}
```

[GetLocationKind](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostfield-getlocationkind)

The GetLocationKind method returns what kind of location the symbol is at according to the LocationKind enumeration. Such enumeration can be one of the following values: 

Enumerant | Meaning
|---------|--------|
LocationMember | The field is a regular data member of a class, structure, union, or other type construct. It has an offset which is relative to base address of the containing type construct. Such base address is typically represented by the this pointer. The offset of the field can be retrieved via the GetOffset method. The GetLocation and GetValue methods will fail for a field which is LocationMember.
LocationStatic | The field is static and has its own address. The GetLocation method will return the abstract location (e.g.: address) of the static field. The GetOffset and GetValue methods will fail for a field which is LocationStatic.
LocationConstant | The field is a constant and has a value. The GetValue method will return the value of the constant. The GetOffset and GetLocation methods will fail for a field which is LocationConstant
LocationNone | The field has no location. It may have been optimized out by the compiler or it may be a static field which is declared but never defined. Regardless of how such a field came to be, it has no physical presence or value. It is only in the symbols. All acquisition methods (GetOffset, GetLocation, and GetValue) will fail for a field which is LocationNone.

[GetOffset](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostfield-getoffset)

For fields which have an offset (e.g.: fields whose location kind indicates LocationMember), the GetOffset method will return the offset from the base address of the containing type (the this pointer) to the data for the field itself. Such offsets are always expressed as unsigned 64-bit values. 
If the given field does not have a location which is an offset from the base address of the containing type, the GetOffset method will fail. 

[GetLocation](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostfield-getlocation)

For fields which have an address regardless of the particular type instance (e.g.: fields whose location kind indicates LocationStatic), the GetLocation method will return the abstract location (address) of the field. 
If the given field does not have a static location, the GetLocation method will fail. 

[GetValue](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostfield-getvalue)

For fields which have a constant value defined within the symbolic information (e.g.: fields whose location kind indicates LocationConstant), the GetValue method will return the constant value of the field. 
If the given field does not have a constant value, the GetValue method will fail. 


**Free Data Access: IDebugHostData**

Data in modules which is not a member of another type is represented by the IDebugHostData interface. That interface is defined as follows (ignoring methods generic to IDebugHostSymbol): 

```cpp
DECLARE_INTERFACE_(IDebugHostData, IDebugHostSymbol)
{
    STDMETHOD(GetLocationKind)(_Out_ LocationKind *locationKind) PURE;
    STDMETHOD(GetLocation)(_Out_ Location* location) PURE;
    STDMETHOD(GetValue)(_Out_ VARIANT* value) PURE;
}
```

All of these methods are semantically equivalent to their counterparts in IDebugHostField. The only difference is that the GetLocationKind method will never return LocationMember for free data. 

[GetLocationKind](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostdata-getlocationkind)

The GetLocationKind method returns what kind of location the symbol is at according to the LocationKind enumeration. The description of this enumeration can be found in the documentation for IDebugHostField. 

[GetLocation](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostdata-getlocation)

For data which has an address, the GetLocation method will return the abstract location (address) of the field. 
If the given data does not have a static location, the GetLocation method will fail. 

[GetValue](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostdata-getvalue)

For datawhich has a constant value defined within the symbolic information (e.g.: data whose location kind indicates LocationConstant), the GetValue method will return the constant value of the field. 
If the given data does not have a constant value, the GetValue method will fail. 


**Base Classes: IDebugHostBaseClass**

The inheritance hierarchy of a given type is expressed through children of a type symbol. If a given type derives (inheritance wise) from one or more types, there will be one or more SymbolBaseClass children of the type symbol for the type. Each of those SymbolBaseClass symbols represent immediate inheritance from a particular type. The name of the base class is both the name of the SymbolBaseClass symbol as well as that of the type symbol for the base class. The GetType method on the SymbolBaseClass symbol can be used to get the type symbol for the base class itself. 
The full inheritance hierarchy can be traversed by recursively exploring SymbolBaseClass child symbols. 
Each of these base class symbols is expressed by the IDebugHostBaseClass interface which is defined as follows (ignoring methods generic to IDebugHostSymbol): 

```cpp
DECLARE_INTERFACE_(IDebugHostBaseClass, IDebugHostSymbol)
{
    STDMETHOD(GetOffset)(_Out_ ULONG64* offset) PURE;
}
```

[GetOffset](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostbaseclass-getoffset)

The GetOffset method returns the offset of the base class from the base address of the derived class. Such offset may be zero or may be a positive unsigned 64-bit value. 


**Public Symbols: IDebugHostPublic**

Public symbols represent things in the public table within a symbol file. They are, in effect, export addresses. There is no type information associated with a public symbol -- only an address. Unless a public symbol is explicitly requested by the caller, the debug host prefers to return private symbols for every inquiry. A public symbol is expressed by the IDebugHostPublic interface which is defined as follows (ignoring methods which are generic to IDebugHostSymbol): 

```cpp
DECLARE_INTERFACE_(IDebugHostPublic, IDebugHostSymbol)
{
    STDMETHOD(GetLocationKind)(_Out_ LocationKind *locationKind) PURE;
    STDMETHOD(GetLocation)(_Out_ Location* location) PURE;
}
```

All of these methods are semantically equivalent to their counterparts in IDebugHostField. The only difference is that the GetLocationKind method will never return LocationMember or LocationConstant for such symbols. 

[GetLocationKind](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostpublic-getlocationkind)

The GetLocationKind method returns what kind of location the symbol is at according to the LocationKind enumeration. The description of this enumeration can be found in the documentation for IDebugHostField. 

[GetLocation](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostpublic-getlocation)

For data which has an address, the GetLocation method will return the abstract location (address) of the field. 
If the given public does not have a static location, the GetLocation method will fail. 


**Module Signatures and Version Matching: IDebugHostModuleSignature**

Module signatures represent a means to check whether a given module meets a set of criteria regarding naming and versioning. A module signature is created via the CreateModuleSignature method on IDebugHostSymbols. It can match the module name, and an optional range of version numbers for the module. Once such a signature is created, the client receives an IDebugHostModuleSignature interface which is defined as follows: 

```cpp
DECLARE_INTERFACE_(IDebugHostModuleSignature, IUnknown)
{
    STDMETHOD(IsMatch)(_In_ IDebugHostModule* pModule, _Out_ bool* isMatch) PURE;
}
```

[IsMatch](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughostmodulesignature-ismatch)

The IsMatch method compares a particular module (as given by an IDebugHostModule symbol) against a signature, comparing the module name and version to the name and version range indicated in the signature. An indication of whether the given module symbol matches the signature is returned. 

**Type Signatures and Type Matching: IDebugHostTypeSignature**

Type signatures represent a means to check whether a given type instance meets a set of criteria about the name of the type, the generic arguments to the type, and the module that the type is located within. A type signature is created via the CreateTypeSignature method on IDebugHostSymbols. Once such a signature is created, the client receives an IDebugHostTypeSignature interface which is defined as follows: 

```cpp
DECLARE_INTERFACE_(IDebugHostTypeSignature, IUnknown)
{
    STDMETHOD(GetHashCode)(_Out_ ULONG* hashCode) PURE;
    STDMETHOD(IsMatch)(_In_ IDebugHostType* type, _Out_ bool* isMatch, _COM_Outptr_opt_ IDebugHostSymbolEnumerator** wildcardMatches) PURE;
    STDMETHOD(CompareAgainst)(_In_ IDebugHostTypeSignature* typeSignature, _Out_ SignatureComparison* result) PURE;
}
```

[GetHashCode](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttypesignature-gethashcode)

The GetHashCode method returns a 32-bit hash code for the type signature. The debug host guarantees that there is synchronization in implementation between the hash code returned for type instances and the hash code returned for type signatures. With the exception of a global match, if a type instance is capable of matching a type signature, both will have the same 32-bit hash code. This allows an initial rapid comparison and match between a type instance and a plethora of type signatures registered with the data model manager. 

[IsMatch](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttypesignature-ismatch)

The IsMatch method returns an indication of whether a particular type instance matches the criteria specified in the type signature. If it does, an indication of this is returned as well as an enumerator which will indicate all of the specific portions of the type instance (as symbols) which matched wildcards in the type signature. 

[CompareAgainst](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgmodel/nf-dbgmodel-idebughosttypesignature-compareagainst)

The CompareAgainst method compares the type signature to another type signature and returns how the two signatures compare. The comparison result which is returned is a member of the SignatureComparison enumeration which is defined as follows: 

Enumerant | Meaning
|---------|-----------|
Unrelated | There is no relationship between the two signatures or types being compared.
Ambiguous |One signature or type compares ambiguously against the other. For two type signatures, this means that there are potential type instances which could match either signature equally well. As an example, the two type signatures shown below are ambiguous.  Signature 1: `std::pair<*, int>`  Signature 2: `std::pair<int,*>` because the type instance `std::pair<int, int>` matches either one equally well (both have one concrete and one wildcard match).
LessSpecific | One signature or type is less specific than the other. Often, this means that the less specific signature has a wildcard where the more specific one has a concrete type. As an example, the first signature below is less specific than the second. Signature 1: `std::pair<*, int>` Signature 2: `std::pair<int, int>` because it has a wildcard (the `*`) where the second has a concrete type (int).
MoreSpecific | One signature or type is more specific than the other. Often, this means that the more specific signature has a concrete type where the less specific one has a wildcard. As an example, the first signature below is more specific than the second. Signature 1:  `std::pair<int, int>` Signature 2: `std::pair<*, int>` because it has a concrete type (int) where the second has a wildcard (the `*`).
Identical | The two signatures or types are identical.







---

## <span id="related_topics"></span>Related topics

[Debugger Data Model C++ Overview](data-model-cpp-overview.md)

[Debugger Data Model C++ Interfaces](data-model-cpp-interfaces.md)

[Debugger Data Model C++ Objects](data-model-cpp-objects.md)

[Debugger Data Model C++ Additional Interfaces](data-model-cpp-additional-interfaces.md)

[Debugger Data Model C++ Concepts](data-model-cpp-concepts.md)

[Debugger Data Model C++ Scripting](data-model-cpp-scripting.md)
