---
title: Debugger Data Model C++ Interfaces Overview
description: This topic provides an overview of the Debugger Data Model C++ Interfaces to extend and customize the capabilities of the debugger.
ms.author: domars
ms.date: 07/13/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugger Data Model C++ Interfaces Overview

This topic provides an overview of how to use Debugger Data Model C++ Interfaces to extend and customize the capabilities of the debugger.

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

[Overview of Debugger Data Model C++ Interfaces](#overview)

[Summary of Debugger Data Model Interfaces](#summary)

---

## <span id="overview"> Overview of Debugger Debugger Data Model C++ Interfaces

The debugger data model is an extensible object model that is central to the way in which new debugger extensions (including those in JavaScript, NatVis, and C++) both consume information from the debugger and produce information that can be accessed from the debugger as well as other extensions. Constructs which are written to the data model APIs are available in the debugger's newer (dx) expression evaluator as well as from JavaScript extensions or other C++ extensions for that matter. 


ToDo: Add more overview content here.



## <span id="summary"> Summary of Debugger Data Model Interfaces

There are a multitude of C++ interfaces which comprise different pieces of the data model. In order to approach these interfaces in a consistent and easy manner, they are broken down by general category. The main areas here: 

**The General Object Model**

The first and most important set of interfaces define how to get access to the core data model and how to access and manipulate objects. IModelObject is the interface which represents every object in the data model (much like C#'s object). This is the main interface of interest for both consumers of and producers to the data model. The other interfaces are mechanisms for accessing different aspects of objects. 
The following interfaces are defined for this category: 


*Bridges Between DbgEng and the Data Model*

[IHostDataModelAccess](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-ihostdatamodelaccess?branch=rs5) 

*Main Interfaces* 

[IModelObject](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-imodelobject?branch=rs5) 

[IKeyStore](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-ikeystore?branch=rs5) 

[IModelIterator](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-imodeliterator?branch=rs5) 

[IModelPropertyAccessor](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-imodelpropertyaccessor?branch=rs5) 

[IModelMethod](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-imodelmethod?branch=rs5) 

[IKeyEnumerator](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-ikeyenumerator?branch=rs5) 

[IRawEnumerator](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-irawenumerator?branch=rs5) 

[IModelKeyReference](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-imodelkeyreference?branch=rs5)  / [IModelKeyReference2](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-imodelkeyreference2?branch=rs5) 

*Concept Interfaces*

[IStringDisplayableConcept](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-istringdisplayableconcept?branch=rs5) 

[IIterableConcept](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-iiterableconcept?branch=rs5) 

[IIndexableConcept](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-iindexableconcept?branch=rs5) 

[IPreferredRuntimeTypeConcept](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-ipreferredruntimetypeconcept?branch=rs5) 

[IDataModelConcept](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-idatamodelconcept?branch=rs5) 

[IDynamicKeyProviderConcept](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-idynamickeyproviderconcept?branch=rs5) 

[IDynamicConceptProviderConcept](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/dbgmodel/nn-dbgmodel-idynamicconceptproviderconcept?branch=rs5) 


**Management of Data Models and Extensibility**

The Data Model Manager is the core component which manages how all extensibility occurs. It is the central repository of a set of tables which map both native types to extension points as well as synthetic constructs to extension points. In addition, it is the entity which is responsible for the boxing of objects (conversion of ordinal values or strings into IModelObject's). 

The following interfaces are defined for this category: 

*General Data Model Manager Access* 

[IDataModelManager]()  / [IDataModelManager2]() 

*Script Management* 

[IDataModelScriptManager]() 

[IDataModelScriptProviderEnumerator]() 


**Access to the Debugger's Type System and Memory Spaces**

The underlying type system and memory spaces of the debugger are exposed in detail for extensions to make use of. 
The following interfaces are defined for this category: 

*General Host (Debugger) Interfaces*

[IDebugHost]() 

[IDebugHostStatus]() 

[IDebugHostContext]() 

[IDebugHostMemory]()  / [IDebugHostMemory2]() 

[IDebugHostErrorSink]() 

[IDebugHostEvaluator]()  / [IDebugHostEvaluator2]() 

[IDebugHostExtensibility]() 

*Host (Debugger) Type System Interfaces* 

[IDebugHostSymbols]() 

[IDebugHostSymbol]()  / [IDebugHostSymbol2]() 

[IDebugHostModule]() 

[IDebugHostType]()  / [IDebugHostType2]() 

[IDebugHostConstant]() 

[IDebugHostField]() 

[IDebugHostData]() 

[IDebugHostBaseClass]() 

[IDebugHostPublic]() 

[IDebugHostModuleSignature]() 

[IDebugHostTypeSignature]() 

*Host (Debugger) Support for Scripting* 

[IDebugHostScriptHost]() 


**Authoring and Consuming Scripts**

The Data Model also has a general notion of what a script is and how to debug one. It is entirely possible for a debugger extension to come along and define a general bridge between the data model and another dynamic language (usually a scripting environment). This set of interfaces is how that is accomplished as well as how a debugger UI can make use of such scripts. 

The following interfaces are defined for this category: 

*General Script Interfaces* 

[IDataModelScriptProvider]() 

[IDataModelScript]() 

[IDataModelScriptClient]() 

[IDataModelScriptHostContext]() 

[IDataModelScriptTemplate]() 

[IDataModelScriptTemplateEnumerator]() 

[IDataModelNameBinder]() 


*Script Debugger Interfaces* 

[IDataModelScriptDebug]() 

[IDataModelScriptDebugClient]() 

[IDataModelScriptDebugStack]() 

[IDataModelScriptDebugStackFrame]() 

[IDataModelScriptDebugVariableSetEnumerator]() 

[IDataModelScriptDebugBreakpoint]() 

[IDataModelScriptDebugBreakpointEnumerator]() 








---

## <span id="related_topics"></span>Related topics

[JavaScript Debugger Example Scripts](javascript-debugger-example-scripts.md)

[Native Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md)