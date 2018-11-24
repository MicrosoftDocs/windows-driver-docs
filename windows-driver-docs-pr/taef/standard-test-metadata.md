---
title: Standard Test Metadata
description: Standard Test Metadata
ms.assetid: A95FC176-B3A1-4bbf-833E-411CDE73C571
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standard Test Metadata


The following Test 'mark-up' metadata is standard metadata that can be applied to TAEF tests.

## <span id="Implicit_Metadata"></span><span id="implicit_metadata"></span><span id="IMPLICIT_METADATA"></span>Implicit Metadata


Certain pieces of metadata are automatically inferred from the markup of the tests:

-   "Name" - the fully qualified name of the test.
-   "Architecture" - the processor architecture of the DLL. This value will be one of 'x86', 'x64' or 'arm'.
-   "TestFile" - The DLL file that the test was described in.

## <span id="Selection_Metadata"></span><span id="selection_metadata"></span><span id="SELECTION_METADATA"></span>Selection Metadata


The selection metadata are simply 'preferred' pieces of metadata to allow teams to have a standard to allow them to better consume one another's tests. There is no required metadata - mandating metadata increases the cost of adding automation, and all metadata should be optional, or should enable 'opt-in' behavior.

There are cases when multiple values can be specified for a metadata value, in which case you should use a semicolon-separated list, and use a 'contains' style selection query, to test for it. For example, if the "Owner" metadata needs two values, then it should be set to "Someone;SomeoneElse". The query to select tests that are owned only by Someone would be:

``` syntax
te Wex.Common.Tests.dll /select:@Owner='Someone'
```

Whereas, the following query would select tests that are owned or co-owned by Someone:

``` syntax
te Wex.Common.Tests.dll /select:@Owner='*Someone*'
```

You can define your own metadata to use within your own company. The following suggestions are recommendations. .

## <span id="_You_should...__Metadata"></span><span id="_you_should...__metadata"></span><span id="_YOU_SHOULD...__METADATA"></span>"You should..." Metadata


These metadata properties are recommendations and have clear meanings. Use these metadata properties as you need them:

<span id="_ActivationContext_"></span><span id="_activationcontext_"></span><span id="_ACTIVATIONCONTEXT_"></span>"ActivationContext"  
Specifies a particular version of binary from various side-by-side assemblies in the system. See [Activation Context](activation-context.md) for details.

<span id="_BinaryUnderTest_"></span><span id="_binaryundertest_"></span><span id="_BINARYUNDERTEST_"></span>"BinaryUnderTest"  
The binary that a given test is \[unit\] testing. This allows developers to quickly run all unit tests that verify a given DLL.

<span id="_DefaultTestResult_"></span><span id="_defaulttestresult_"></span><span id="_DEFAULTTESTRESULT_"></span>"DefaultTestResult"  
Overrides the default test result of "Passed" for the given test. If the test passes, the logged result will be the default test result. Possible values are "Passed", "Failed", "NotRun", "Blocked" and "Skipped".

<span id="_DeploymentItem_"></span><span id="_deploymentitem_"></span><span id="_DEPLOYMENTITEM_"></span>["DeploymentItem"](deploymentitem-metadata.md)  
Identifies files and folders as test dependencies.

<span id="_Description_"></span><span id="_description_"></span><span id="_DESCRIPTION_"></span>"Description"  
A short description of what the test does.

<span id="_DpiAware_"></span><span id="_dpiaware_"></span><span id="_DPIAWARE_"></span>"DpiAware"  
When set to "true," TAEF will run your tests in a process marked as DPI-aware, see [High DPI](https://msdn.microsoft.com/library/windows/desktop/dd464646).

<span id="_ExecutionGroup_"></span><span id="_executiongroup_"></span><span id="_EXECUTIONGROUP_"></span>"ExecutionGroup"  
A set of consecutive tests within a class that need to be run in order and are blocked if a previous test in the execution group is not run or fails. See [Execution Groups](execution-groups.md) for details.

<span id="_Ignore_"></span><span id="_ignore_"></span><span id="_IGNORE_"></span>"Ignore"  
Test classes or test methods with "Ignore" metadata set to "true" are skipped during execution or listing by TAEF. To override this behavior and run or list all tests including the ones with "Ignore" metadata, specify **/runIgnoredTests** as a command-line argument.

<span id="_IsolationLevel_"></span><span id="_isolationlevel_"></span><span id="_ISOLATIONLEVEL_"></span>"IsolationLevel"  
Specifies the minimum level of isolation to be used when executing TAEF tests. See [Test Isolation](test-isolation.md) for more details.

<span id="_Parallel_"></span><span id="_parallel_"></span><span id="_PARALLEL_"></span>["Parallel"](parallel.md)  
Executes tests in parallel across multiple processors. For more details, see [Parallel](parallel.md).

<span id="_Priority_"></span><span id="_priority_"></span><span id="_PRIORITY_"></span>"Priority"  
The priority of the test as an integer, smaller is high-priority.

<span id="_RebootPossible_"></span><span id="_rebootpossible_"></span><span id="_REBOOTPOSSIBLE_"></span>["RebootPossible"](reboot.md)  
When set to true, enables the use of the Reboot APIs to request TAEF perform a computer restart or inform TAEF of an impending test-initiated restart.

<span id="_RunAs_"></span><span id="_runas_"></span><span id="_RUNAS_"></span>"RunAs"  
Specifies the context in which the tests in concern should be run. See [RunAs Execution](runas.md) for details.

<span id="_RunFixtureAs_"></span><span id="_runfixtureas_"></span><span id="_RUNFIXTUREAS_"></span>["RunFixtureAs"](runfixtureas.md)  
Specifies the context in which the test fixtures in concern should be run. See [RunFixtureAs](runfixtureas.md) for details.

<span id="_TestClassification_Scope_"></span><span id="_testclassification_scope_"></span><span id="_TESTCLASSIFICATION_SCOPE_"></span>"TestClassification:Scope"  
The Test Classification "Scope" identifies the test collateral used to validate "engineering process events" that occur in Windows.

<span id="_TestClassification_Type_"></span><span id="_testclassification_type_"></span><span id="_TESTCLASSIFICATION_TYPE_"></span>"TestClassification:Type"  
Test Classification "Type" identifies the types of tests that need to be distinguished.

<span id="_TestClassification_"></span><span id="_testclassification_"></span><span id="_TESTCLASSIFICATION_"></span>"TestClassification"  
Use property value "Unit:WUTG" to indicate a unit test that conforms to Windows Unit Testing Guidelines (WUTG). Use property value "Unit:WUTG:ChexGate" to indicate a unit test that conforms to Windows Unit Testing Guidelines (WUTG) and should run during gated phase of Chex scenario (failure blocking submit).

<span id="_TestTimeout_"></span><span id="_testtimeout_"></span><span id="_TESTTIMEOUT_"></span>"TestTimeout"  
Specifies the maximum amount of time a given test or setup/cleanup method can take. See [Timeouts](taef-timeouts.md) for details.

<span id="_ThreadingModel_"></span><span id="_threadingmodel_"></span><span id="_THREADINGMODEL_"></span>"ThreadingModel"  
The pre-configured COM threading model used by the test. See [Configuring Threading Models](threading-models.md) for details.

Data-driven testing related:

<span id="_DataSource_"></span><span id="_datasource_"></span><span id="_DATASOURCE_"></span>"DataSource"  
Specifies the main source for data for [data-driven tests](data-driven-testing.md).

<span id="_TableId_"></span><span id="_tableid_"></span><span id="_TABLEID_"></span>"TableId"  
Specifies the name or Id of the Table separate from the "DataSource" in case of [Table-Based Data-driven tests](table-data-source.md).

<span id="_Pict_Timeout___and_deprecated__PictTimeout__"></span><span id="_pict_timeout___and_deprecated__picttimeout__"></span><span id="_PICT_TIMEOUT___AND_DEPRECATED__PICTTIMEOUT__"></span>"Pict:Timeout" (and deprecated "PictTimeout")  
Overrides the default time-out of 5 minutes allowed for PICT.exe to process the user specified model file in case of [PICT based data-driven tests](pict-data-source.md).

<span id="_Pict_SeedingFile___and_deprecated__Seed__"></span><span id="_pict_seedingfile___and_deprecated__seed__"></span><span id="_PICT_SEEDINGFILE___AND_DEPRECATED__SEED__"></span>"Pict:SeedingFile" (and deprecated "Seed")  
Specified the relative location to the seed file, separate from the "DataSource" in case of [PICT based data-driven tests](pict-data-source.md).

<span id="_Pict_Order_"></span><span id="_pict_order_"></span><span id="_PICT_ORDER_"></span>"Pict:Order"  
Specifies the value of the /o parameter for PICT.exe when it is called in [PICT based data-driven tests](pict-data-source.md).

<span id="_Pict_ValueSeparator_"></span><span id="_pict_valueseparator_"></span><span id="_PICT_VALUESEPARATOR_"></span>"Pict:ValueSeparator"  
Specifies the value of the /d parameter for PICT.exe when it is called in [PICT based data-driven tests](pict-data-source.md).

<span id="_Pict_AliasSeparator_"></span><span id="_pict_aliasseparator_"></span><span id="_PICT_ALIASSEPARATOR_"></span>"Pict:AliasSeparator"  
Specifies the value of the /a parameter for PICT.exe when it is called in [PICT based data-driven tests](pict-data-source.md).

<span id="_Pict_NegativeValuePrefix_"></span><span id="_pict_negativevalueprefix_"></span><span id="_PICT_NEGATIVEVALUEPREFIX_"></span>"Pict:NegativeValuePrefix"  
Specifies the value of the /n parameter for PICT.exe when it is called in [PICT based data-driven tests](pict-data-source.md).

<span id="_Pict_Random_"></span><span id="_pict_random_"></span><span id="_PICT_RANDOM_"></span>"Pict:Random"  
Specifies whether randomness should be used when calling PICT.exe for [PICT based data-driven tests](pict-data-source.md). When this is true, the random seed that was used is logged by TAEF.

<span id="_Pict_RandomSeed_"></span><span id="_pict_randomseed_"></span><span id="_PICT_RANDOMSEED_"></span>"Pict:RandomSeed"  
Specifies the value of the /r parameter for PICT.exe when it is called in [PICT based data-driven tests](pict-data-source.md). Setting this changes the default for "Pict:Random" from false to true.

<span id="_Pict_CaseSensitive_"></span><span id="_pict_casesensitive_"></span><span id="_PICT_CASESENSITIVE_"></span>"Pict:CaseSensitive"  
Specifies whether the /c parameter should be used for PICT.exe when it is called in [PICT based data-driven tests](pict-data-source.md).

Support for Device related:

<span id="_TestResourceDependent_"></span><span id="_testresourcedependent_"></span><span id="_TESTRESOURCEDEPENDENT_"></span>"TestResourceDependent"  
Specifies that the tests in current scope are dependent on the TestResource and function on the resources collected by BuildResourceList(...). See [Support for Devices](device-support.md) for details.

<span id="_ResourceSelection_"></span><span id="_resourceselection_"></span><span id="_RESOURCESELECTION_"></span>"ResourceSelection"  
Specifies the query to match TestResources collected by BuildResourceList(...) which are relevant for the tests in question. See [Support for Devices](device-support.md) for details.

## <span id="_You_can...__Metadata"></span><span id="_you_can...__metadata"></span><span id="_YOU_CAN...__METADATA"></span>"You can..." Metadata


These metadata properties can be used, but their interpretation is not guaranteed; teams can use them if they want to.

<span id="_Owner_"></span><span id="_owner_"></span><span id="_OWNER_"></span>"Owner"  
The alias of the owner of the test.

<span id="_ProcessUnderTest_"></span><span id="_processundertest_"></span><span id="_PROCESSUNDERTEST_"></span>"ProcessUnderTest"  
Useful for runtime analysis. For example, if a test is testing "Explorer.exe", then run Radar (a runtime analysis tool) against the process.

<span id="_Feature_"></span><span id="_feature_"></span><span id="_FEATURE_"></span>"Feature"  
An identifier that categorizes the test to a specific feature or technology. This should be treated as a 'cookie' identifier who's interpretation is down to the team that defines it.

## <span id="_Reserved__Metadata"></span><span id="_reserved__metadata"></span><span id="_RESERVED__METADATA"></span>'Reserved' Metadata


The following metadata may be used in the future - please don't use it.

-   User
-   IntegrityLevel
-   Timeout
-   HostType

 

 





