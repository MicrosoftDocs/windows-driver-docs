---
title: Debugger Data Model C++ Interfaces Overview
description: This topic provides an overview of the Debugger Data Model C++ Interfaces to extend and customize the capabilities of the debugger.
ms.date: 09/12/2019
---

# Debugger Data Model C++ Overview

This topic provides an overview of how to use Debugger Data Model C++ Interfaces to extend and customize the capabilities of the debugger.

This topic is part of a series which describes the interfaces accessible from C++, how to use them to build a C++ based debugger extension, and how to make use of other data model constructs (e.g.: JavaScript or NatVis) from a C++ data model extension.

[Debugger Data Model C++ Overview](data-model-cpp-overview.md)

[Debugger Data Model C++ Interfaces](data-model-cpp-interfaces.md)

[Debugger Data Model C++ Objects](data-model-cpp-objects.md)

[Debugger Data Model C++ Additional Interfaces](data-model-cpp-additional-interfaces.md)

[Debugger Data Model C++ Concepts](data-model-cpp-concepts.md)

[Debugger Data Model C++ Scripting](data-model-cpp-scripting.md)

---

## <span id="overview"> Overview of the Debugger Data Model C++ Interface

The debugger data model is an extensible object model that is central to the way in which new debugger extensions (including those in JavaScript, NatVis, and C++) both consume information from the debugger and produce information that can be accessed from the debugger as well as other extensions. Constructs which are written to the data model APIs are available in the debugger's newer (dx) expression evaluator as well as from JavaScript extensions or C++ extensions. 

To illustrate the goals of the debugger data model, consider this traditional debugger command.

```console
0: kd> !process 0 0 
PROCESS ffffe0007e6a7780
    SessionId: 1  Cid: 0f68    Peb: 7ff7cfe7a000  ParentCid: 0f34
    DirBase: 1f7fb9000  ObjectTable: ffffc001cec82780  HandleCount:  34.
    Image: echoapp.exe
...
```
The debugger command is using a binary mask and it provides text only output in non-standard ways. The text output is difficult to consume, format, or extend and the layout is specific to this command.

Contrast this to  the debugger data model [dx (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md) command.

```console
dx @$cursession.Processes.Where(p => p.Threads.Count() > 5)
```
This command uses a standard data model that is discoverable, extensible and composable in uniform ways.

Logically name spacing things and extending on specific objects allows for the discovery of debugger extension functionality.  

> [!TIP]
> Because the Data Model C++ Object interfaces can be very verbose to implement a full C++ helper library for the data model which uses a full C++ exception and template programming paradigm is recommended. For more information, see [Using the DbgModelClientEx Library](#dbgmodelclientex) later in this topic.
>

The data model is the way that the new [WinDbg Preview](debugging-using-windbg-preview.md) debugger, shows most things. Many elements in the new UI can be queried, extended, or scripted, because they are powered by the data model. For more information, see [WinDbg Preview - Data Model](windbg-data-model-preview.md).

![Data model explore window showing process and threads.](images/windbgx-data-model-process-threads.png)


### Data Model Architectural View

The following diagram summarizes the major elements of the debugger data model architecture.

- To the left side, UI elements are shown that provide access to the objects and support such functionality as LINQ queries.  
- On the right side of the diagram are components that provide data to debugger data model. This includes custom NatVis, JavaScript and C++ debugger data model extensions. 

![Data model architectural view showing common object model in the center and providers on the right.](images/data-model-simple-architectural-view.png)


### Object Model

At the center of the Debugger Data Model is a uniform object representation in which everything is an instance of the IModelObject interface.  While such an object may represent an intrinsic (e.g.: an integer value) or another data model interface, it often represents a dynamic object – a dictionary of key/value/metadata tuples and a set of concepts which describe abstract behaviors.   

This diagram shows how the IModelObject uses Key Stores to contain values that a provider can create, register and manipulate.

- It shows a *provider*, that provides information to the object model
- On the left it shows the *IModelObject*, that is the common object model that is used to manipulate objects.
- In the center is the *Key Store* that is used to store and access values.
- At the bottom it shows *Concepts* that support objects with functionality such as the ability to convert to a displayable string or be indexed.

![Data model architectural view showing IModelObject as input and a tuples key store.](images/data-model-object-model.png)


### The Data Model: A Consumer View

The next diagram shows a consumer view of the data model. In the example the [dx (Display Debugger Object Model Expression)](./dx--display-visualizer-variables-.md) command is being used to query information. 

- The Dx command communicates through a serializer to the object enumeration interface. 
- IDebugHost* objects are used to gather information from the debugger engine. 
- Expression and semantic evaluators are used to send the request to the debugger engine.

![Data model architectural view showing UI feeding into evaluators that feed into IDebugHost.](images/data-model-consumer-view.png)


### The Data Model: A Producer View

This diagram shows a producer view of the data model.

- A NatVis provider is shown on the left that consumes XML that defines additional functionality.
- A JavaScript provider can take advantage of *Dynamic Provider Concepts* to manipulate information in real time.
- The bottom shows a native code provider that can also define additional functionality.

![Data model architectural view showing IModelObject on with Natvis, Javascript and Native code consumers.](images/data-model-producer-view.png)

### Data Model Manager

This diagram shows the central role that the data model manager plays in the management of objects.

- The Data Model Manager acts as a central registrar for all objects. 
- On the left it shows how standard debugger elements such as sessions and process are registered.
- The namespace block shows the central registration list.
- The right side of the diagram shows two providers, one for NatVis on the top, and a C/C++ extension on the bottom.

![Data model architectural view showing registered names being looked up by the data model manager.](images/data-model-manager.png)

## <span id="summary"> Summary of Debugger Data Model Interfaces

There are a multitude of C++ interfaces which comprise different pieces of the data model. In order to approach these interfaces in a consistent and easy manner, they are broken down by general category. The main areas here: 

**The General Object Model**

The first and most important set of interfaces define how to get access to the core data model and how to access and manipulate objects. IModelObject is the interface which represents every object in the data model (much like C#'s object). This is the main interface of interest for both consumers of and producers to the data model. The other interfaces are mechanisms for accessing different aspects of objects. 
The following interfaces are defined for this category: 


*Bridges Between DbgEng and the Data Model*

[IHostDataModelAccess](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-ihostdatamodelaccess) 

*Main Interfaces* 

[IModelObject](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-imodelobject) 

[IKeyStore](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-ikeystore) 

[IModelIterator](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-imodeliterator) 

[IModelPropertyAccessor](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-imodelpropertyaccessor) 

[IModelMethod](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-imodelmethod) 

[IKeyEnumerator](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-ikeyenumerator) 

[IRawEnumerator](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-irawenumerator) 

[IModelKeyReference](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-imodelkeyreference)  / [IModelKeyReference2](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-imodelkeyreference2) 

*Concept Interfaces*

[IStringDisplayableConcept](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-istringdisplayableconcept) 

[IIterableConcept](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-iiterableconcept) 

[IIndexableConcept](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-iindexableconcept) 

[IPreferredRuntimeTypeConcept](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-ipreferredruntimetypeconcept) 

[IDataModelConcept](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelconcept) 

[IDynamicKeyProviderConcept](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idynamickeyproviderconcept) 

[IDynamicConceptProviderConcept](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idynamicconceptproviderconcept) 


**Management of Data Models and Extensibility**

The Data Model Manager is the core component which manages how all extensibility occurs. It is the central repository of a set of tables which map both native types to extension points as well as synthetic constructs to extension points. In addition, it is the entity which is responsible for the boxing of objects (conversion of ordinal values or strings into IModelObject's). 

The following interfaces are defined for this category: 

*General Data Model Manager Access* 

[IDataModelManager](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelmanager)  / [IDataModelManager2](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelmanager2) 

*Script Management* 

[IDataModelScriptManager](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscriptmanager) 

[IDataModelScriptProviderEnumerator](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscriptproviderenumerator) 


**Access to the Debugger's Type System and Memory Spaces**

The underlying type system and memory spaces of the debugger are exposed in detail for extensions to make use of. 
The following interfaces are defined for this category: 

*General Host (Debugger) Interfaces*

[IDebugHost](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughost) 

[IDebugHostStatus](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughoststatus) 

[IDebugHostContext](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostcontext) 

[IDebugHostMemory](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostmemory)  / [IDebugHostMemory2](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostmemory2) 

[IDebugHostErrorSink](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughosterrorsink) 

[IDebugHostEvaluator](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostevaluator)  / [IDebugHostEvaluator2](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostevaluator2) 

[IDebugHostExtensibility](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostextensibility) 

*Host (Debugger) Type System Interfaces* 

[IDebugHostSymbols](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostsymbols) 

[IDebugHostSymbol](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostsymbol)  / [IDebugHostSymbol2](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostsymbol2) 

[IDebugHostModule](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostmodule) 

[IDebugHostType](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughosttype)  / [IDebugHostType2](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughosttype2) 

[IDebugHostConstant](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostconstant) 

[IDebugHostField](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostfield) 

[IDebugHostData](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostdata) 

[IDebugHostBaseClass](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostbaseclass) 
[IDebugHostPublic](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostpublic) 

[IDebugHostModuleSignature](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostmodulesignature) 

[IDebugHostTypeSignature](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughosttypesignature) 

*Host (Debugger) Support for Scripting* 

[IDebugHostScriptHost](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idebughostscripthost) 


**Authoring and Consuming Scripts**

The Data Model also has a general notion of what a script is and how to debug one. It is entirely possible for a debugger extension to come along and define a general bridge between the data model and another dynamic language (usually a scripting environment). This set of interfaces is how that is accomplished as well as how a debugger UI can make use of such scripts. 

The following interfaces are defined for this category: 

*General Script Interfaces* 

[IDataModelScriptProvider](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscript) 

[IDataModelScript](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscript) 

[IDataModelScriptClient](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscriptclient) 

[IDataModelScriptHostContext](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscripthostcontext) 

[IDataModelScriptTemplate](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscripttemplate) 

[IDataModelScriptTemplateEnumerator](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscripttemplateenumerator) 

[IDataModelNameBinder](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelnamebinder) 


*Script Debugger Interfaces* 

[IDataModelScriptDebug](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscriptdebug) 

[IDataModelScriptDebugClient](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscriptdebugclient) 

[IDataModelScriptDebugStack](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscriptdebugstack) 

[IDataModelScriptDebugStackFrame](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscriptdebugstackframe) 

[IDataModelScriptDebugVariableSetEnumerator](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscriptdebugvariablesetenumerator) 

[IDataModelScriptDebugBreakpoint](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscriptdebugbreakpoint) 

[IDataModelScriptDebugBreakpointEnumerator](/windows-hardware/drivers/ddi/dbgmodel/nn-dbgmodel-idatamodelscriptdebugbreakpointenumerator) 


## <span id="dbgmodelclientex"> Using the DbgModelClientEx Library

**Overview**

The Data Model C++ Object Interfaces to the data model can be very verbose to implement. While they allow for full manipulation of the data model, they require implementation of a number of small interfaces to extend the data model (e.g.: an IModelPropertyAccessor implementation for each dynamic fetchable property which is added). In addition to this, the HRESULT based programming model adds a significant amount of boiler plate code that is used for error checking.

In order to minimize some of this work, there is a full C++ helper library for the data model which uses a full C++ exception and template programming paradigm. Use of this library allows for more concise code when consuming or extending the data model and is recommended.

There are two important namespaces in the helper library:

Debugger::DataModel::ClientEx - helpers for consumption of the data model

Debugger::DataModel::ProviderEx - helpers for extension of the data model

For additional information on using the DbgModelClientEx library, see the readme file at this github site:

https://github.com/Microsoft/WinDbg-Libraries/tree/master/DbgModelCppLib


**HelloWorld C++ Sample**

To see how the DbgModelClientEx library can be used, review the Data Model HelloWorld C++ sample here.

https://github.com/Microsoft/WinDbg-Samples/tree/master/DataModelHelloWorld

The sample includes:

- HelloProvider.cpp - This is an implementation of a provider class which adds a new example property "Hello" to the debugger's notion of a process.

- SimpleIntroExtension.cpp - This is a simple debugger extension which adds a new example property "Hello" to the debugger's notion of a process. This extension is written against the Data Model C++17 Helper Library.  It is far preferable to write extensions against this library rather than the raw COM ABI due to the volume (and complexity) of glue code which is required.


**JavaScript and COM Samples**

In order to better understand the varying ways to write a debugger extension with the data model, there are three versions of the data model HelloWorld extension available here:

https://github.com/Microsoft/WinDbg-Samples/tree/master/DataModelHelloWorld

- JavaScript - A version written in JavaScript

- C++17 - A version written against the Data Model C++17 Client Library

- COM - A version written against the raw COM ABI (only using WRL for COM helpers)

---

## <span id="related_topics"></span>Related topics

[Debugger Data Model C++ Interfaces](data-model-cpp-interfaces.md)

[Debugger Data Model C++ Objects](data-model-cpp-objects.md)

[Debugger Data Model C++ Additional Interfaces](data-model-cpp-additional-interfaces.md)

[Debugger Data Model C++ Concepts](data-model-cpp-concepts.md)

[Debugger Data Model C++ Scripting](data-model-cpp-scripting.md)