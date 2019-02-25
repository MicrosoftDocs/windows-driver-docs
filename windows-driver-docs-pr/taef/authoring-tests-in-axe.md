---
title: Authoring Tests in AXE
description: Authoring Tests in AXE
ms.assetid: B042FE1B-98E4-48ae-BE2C-15C71EC6640A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Authoring Tests in AXE


TAEF supports authoring tests that are executed with the Assessment Execution Engine (AXE).

AXE support in TAEF enables TAEF to execute AXE assessment manifests. It is primarily designed to wrap legacy tests, written as command line EXEs, into XML-based AXE assessment manifests. In this way, these legacy tests become executable with TAEF without having to rewrite the tests to TAEF native, managed, or script tests.

## <span id="AXE_Tests_Layout"></span><span id="axe_tests_layout"></span><span id="AXE_TESTS_LAYOUT"></span>AXE Tests Layout


Although regular TAEF test files can contain multiple test classes and tests, TAEF AXE tests (tests that are defined by an AXE assessment manifest) can contain only a single test because the manifest wraps a single executable. Thus, when viewing tests in a TAEF AXE test file, you will always see that the test file (which is the AXE assessment manifest you are viewing), contains a single test class and a single test:

``` syntax
te Examples\AXE.Basic.Examples.manifest /list
Test Authoring and Execution Framework v2.7 Build 6.2.7918.0 (1320) For x64


        D:\enddev2.binaries.amd64chk\Test\CuE\TestExecution\Examples\AXE.Basic.Examples.manifest
            Basic
                Basic::Basic

```

AXE tests also do not support any setup or cleanup methods.

## <span id="Authoring_AXE_Tests"></span><span id="authoring_axe_tests"></span><span id="AUTHORING_AXE_TESTS"></span>Authoring AXE Tests


For AXE tests, TAEF uses the AXE assessment manifest file format.

## <span id="Minimal_AXE_Test_File"></span><span id="minimal_axe_test_file"></span><span id="MINIMAL_AXE_TEST_FILE"></span>Minimal AXE Test File


The AXE assessment manifest schema is designed to support very rich descriptions of complex assessment for sophisticated scenarios. However, the manifests can also be very simple as there are very few mandatory nodes. The following example shows a minimal manifest that includes all of the mandatory tags.

```cpp
1<?xml version="1.0" encoding="utf-8"?>
2<AxeAssessmentManifest xmlns="http://www.microsoft.com/axe/assessment/manifest">
3  <VersionedId>
4    <Guid>{ABCBFDE6-D731-4030-9049-E7CAAB6A6EEE}</Guid>
5    <Version>
6      <Major>1</Major>
7      <Minor>0</Minor>
8      <Build>0</Build>
9      <Revision>0</Revision>
10    </Version>
11  </VersionedId>
12  <MinimumAxeVersionRequired>
13    <Version>
14      <Major>1</Major>
15      <Minor>0</Minor>
16      <Build>1</Build>
17      <Revision>0</Revision>
18    </Version>
19  </MinimumAxeVersionRequired>
20  <Description>
21    <ProgrammaticName>Basic</ProgrammaticName>
22    <DisplayName>Basic Examples</DisplayName>
23    <ToolTip>Sample Basic Examples Assessment Tooltip</ToolTip>
24  </Description>
25  <Meta>
26    <ExitValueMeaning> <ZeroIsSuccess/> </ExitValueMeaning>
27  </Meta>
28  <Execution>
29    <CreateProcess>
30      <ApplicationName>AssessmentSample.exe</ApplicationName>
31    </CreateProcess>
32  </Execution>
33</AxeAssessmentManifest>
```

The AXE test assessment file is an XML file. So, it starts with an ordinary XML header (**line 1**).

**Line 2** identifies the XML file as an AXE manifest.

**Lines 3 - 10** give the test an identity and version that can be used to uniquely identify the test.

**Line 12 - 19** specify the minimum version of AXE that is needed to interpret this manifest and to run the test.

**Lines 20 - 24** give the test a human readable name and a short tooltip description. Note that when you view test properties, your test class name and your test name will correspond to the **ProgrammaticName** element value:

``` syntax
D:\enddev2.binaries.amd64chk\WexTest\CuE\TestExecution>te Examples\AXE.Basic.Examples.manifest /list
Test Authoring and Execution Framework v2.7 Build 6.2.7918.0 (1320) For x64


        D:\enddev2.binaries.amd64chk\Test\CuE\TestExecution\Examples\AXE.Basic.Examples.manifest
            Basic
                Basic::Basic

```

The human readable name is assigned to the **DisplayName** property. This assignment is due to the internal TAEF architecture and design.

``` syntax
Te Examples\AXE.Basic.Examples.manifest /listproperties
Test Authoring and Execution Framework v2.7 Build 6.2.7918.0 (1320) For x64


        D:\enddev2.binaries.amd64chk\Test\CuE\TestExecution\Examples\AXE.Basic.Examples.manifest
                Property[TaefTestType] =  AxeAssessment

            Basic
                Basic::Basic
                        Property[DisplayName] =  Basic Examples
                        Property[ProgrammaticName] =  Basic
                        Property[RunAs] =  Elevated
                        Property[ToolTip] =  Sample Basic Examples Assessment Tooltip

```

This assessment wraps a simple and existing test EXE named **AssessmentSample.exe**. **AssessmentSample.exe** uses the common convention to return a process exit code of zero for success and a non-zero value for failure.

**Lines 25 - 27** tell AXE and TAEF that an exit value of zero means that the test was successful and that any other value means failure.

Finally, **lines 28 - 32** instruct AXE to use the Win32 API CreateProcess() to execute **AssessmentSample.exe**.

## <span id="Using_Metadata_in_AXE_Test_File"></span><span id="using_metadata_in_axe_test_file"></span><span id="USING_METADATA_IN_AXE_TEST_FILE"></span>Using Metadata in AXE Test File


As with any other TAEF test, you can also apply metadata to a TAEF AXE test. Consider the example that is shown below.

```cpp
1<?xml version="1.0" encoding="utf-8"?>
2<AxeAssessmentManifest xmlns="http://www.microsoft.com/axe/assessment/manifest">
3  <VersionedId>
4    <Guid>{F310F3F6-F786-4118-8A18-BC020C7D2521}</Guid>
5    <Version>
6      <Major>1</Major>
7      <Minor>0</Minor>
8      <Build>0</Build>
9      <Revision>0</Revision>
10    </Version>
11  </VersionedId>
12  <MinimumAxeVersionRequired>
13    <Version>
14      <Major>1</Major>
15      <Minor>0</Minor>
16      <Build>1</Build>
17      <Revision>0</Revision>
18    </Version>
19  </MinimumAxeVersionRequired>
20  <Description>
21    <ProgrammaticName>CustomMetadataExamples</ProgrammaticName>
22    <DisplayName>Custom Metadata Examples</DisplayName>
23    <ToolTip>Sample Custom Metadata Examples Assessment Tooltip</ToolTip>
24  </Description>
25  <Properties>
26    <Owner>Someone</Owner>
27    <Priority>1</Priority>
28    <Parallel>false</Parallel>
29  </Properties>
30  <Meta>
31    <ExitValueMeaning> <ZeroIsSuccess/> </ExitValueMeaning>
32  </Meta>
33  <Execution>
34    <CreateProcess>
35      <ApplicationName>AssessmentSample.exe</ApplicationName>
36    </CreateProcess>
37  </Execution>
38</AxeAssessmentManifest>
```

**Lines 25 - 29** demonstrate how TAEF standard and custom metadata can be applied to an AXE test. Under the **AxeAssessmentManifest** XML node is a **Properties** node. Single level XML tags under the **Properties** node are recognized as metadata (properties). All single level XML tags under **Properties** are interpreted as property names and their text values are interpreted as the property values. In the above example, **Owner** is interpreted as a property name and **Someone** as a property value. XML tags with no text in these elements are interpreted as elements whose value equals the empty string (for example, **&lt;SimpleTagWithNoText/&gt;**). Multilevel XML tags under **Properties** are ignored (for example, a multilevel tag like

```cpp
<VerifyOSVersion>
    <Major>6</Major>
    <Minor>0</Minor>
    <Build>0</Build>
</VerifyOSVersion>
```

will be ignored). Similar to any other TAEF tests, you use the **/listProperties** option to display TAEF metadata:

``` syntax
te Examples\AXE.CustomMetadata.Examples.manifest /listProperties
Test Authoring and Execution Framework v2.7 Build 6.2.7918.0 (1320) For x64

        D:\enddev2.binaries.amd64chk\Test\CuE\TestExecution\Examples\AXE.CustomMetadata.Examples.manifest
                Property[TaefTestType] =  AxeAssessment

            CustomMetadataExamples
                CustomMetadataExamples::CustomMetadataExamples
                        Property[DisplayName] =  Custom Metadata Examples
                        Property[Owner] =  Someone
                        Property[Parallel] =  false
                        Property[Priority] =  1
                        Property[ProgrammaticName] =  CustomMetadataExamples
                        Property[RunAs] =  Elevated
                        Property[ToolTip] =  Sample Custom Metadata Examples Assessment Tooltip


```

## <span id="AXE_Tests_Metadata_Support_Limitations"></span><span id="axe_tests_metadata_support_limitations"></span><span id="AXE_TESTS_METADATA_SUPPORT_LIMITATIONS"></span>AXE Tests Metadata Support Limitations


Note: Not all TAEF standard test metadata can be used with TAEF AXE tests.

-   All metadata aimed at modifying the environment in which the process executes, like **ActivationContext** and **ThreadingModel**, will not work with AXE tests. AXE does not use TAEF's process to execute the tests, but creates a new process in which it runs the executable program that is specified by the AXE test file (AXE assessment manifest). For the same reason, data driven TAEF testing (**DataSource** property) does not work with AXE TAEF tests, either.
-   Similarly, because the TAEF AXE test files can encapsulate only a single test, the TAEF metadata that modifies the behavior of a test with regards to other tests, like **ExecutionGroup**, will also not work.
-   Due to the AXE architecture, AXE can only run elevated processes. Therefore, as you saw from TAEF AXE tests' properties above, every TAEF AXE test has **Property\[RunAs\] = Elevated** applied.

## <span id="AXE_Test_File_with_Runtime_Parameters"></span><span id="axe_test_file_with_runtime_parameters"></span><span id="AXE_TEST_FILE_WITH_RUNTIME_PARAMETERS"></span>AXE Test File with Runtime Parameters


TAEF AXE tests also support runtime parameters. To use TAEF's runtime parameters with AXE tests, the parameter names that are to be passed to the executable program need to be defined in the AXE test file.

It is beyond the scope of this document to describe all of the possible AXE manifest parameter features in all details. For that info, please consult the AXE assessment documentation. This document will only cover the most common and useful parameter applications.

The following example shows a more complex AXE assessment manifest.

```cpp
1<?xml version="1.0" encoding="utf-8"?>
2<AxeAssessmentManifest xmlns="http://www.microsoft.com/axe/assessment/manifest">
3  <VersionedId>
4    <Guid>{B63B2FFF-EDEB-41FB-92EA-529CE4A46D20}</Guid>
5    <Version>
6      <Major>1</Major>
7      <Minor>0</Minor>
8      <Build>0</Build>
9      <Revision>0</Revision>
10    </Version>
11  </VersionedId>
12  <MinimumAxeVersionRequired>
13    <Version>
14      <Major>1</Major>
15      <Minor>0</Minor>
16      <Build>1</Build>
17      <Revision>0</Revision>
18    </Version>
19  </MinimumAxeVersionRequired>
20  <Description>
21    <ProgrammaticName>ExplicitRuntimeParameters</ProgrammaticName>
22    <DisplayName>Explicit Runtime Parameters</DisplayName>
23    <ToolTip>Sample Explicit Runtime Parameters Assessment Tooltip</ToolTip>
24  </Description>
25  <ParameterDefinitions>
26    <ParameterDefinition>
27      <Description>
28        <ProgrammaticName>SimpleParameter</ProgrammaticName>
29        <DisplayName>Simple parameter</DisplayName>
30        <ToolTip>The is an example of a simple parameter.</ToolTip>
31      </Description>
32      <Type>
33        <String></String>
34      </Type>
35      <CommandLineFormat>{0}</CommandLineFormat>
36    </ParameterDefinition>
37    <ParameterDefinition>
38      <Description>
39        <ProgrammaticName>RequiredParameterWithoutDefaultValue</ProgrammaticName>
40        <DisplayName>Required parameter without a default value.</DisplayName>
41        <ToolTip>The is an example of a required parameter Without a default value.</ToolTip>
42      </Description>
43      <Required>True</Required>
44      <Type>
45        <Int></Int>
46      </Type>
47      <CommandLineFormat>{0}</CommandLineFormat>
48    </ParameterDefinition>
49    <ParameterDefinition>
50      <Description>
51        <ProgrammaticName>RequiredParameterWithDefaultValue</ProgrammaticName>
52        <DisplayName>Required parameter with a default value</DisplayName>
53        <ToolTip>The is an example of a required parameter With a default value.</ToolTip>
54      </Description>
55      <Required></Required>
56      <DefaultValue>"%AssessmentResultsPath%"</DefaultValue>
57      <Type>
58        <String></String>
59      </Type>
60      <CommandLineFormat>/RequiredParameterWithDefaultValue={0}</CommandLineFormat>
61    </ParameterDefinition>
62  </ParameterDefinitions>
63  <Meta>
64    <ExitValueMeaning> <ZeroIsSuccess/> </ExitValueMeaning>
65  </Meta>
66  <Execution>
67    <CreateProcess>
68      <ApplicationName>AssessmentSample.exe</ApplicationName>
69    </CreateProcess>
70  </Execution>
71</AxeAssessmentManifest>
```

**Lines 25 - 62** are parameter definitions that describe the parameters that are used by TAEF and AXE to pass data into the assessment executable.

The simplest parameter definition is on the **lines 26 - 36**. It consists of a mandatory **Description** section that is exactly the same as the **Description** section for the manifest, which is explained above. Then you see a **Type** tag that defines the parameter data type. (Please consult AXE assessment documentation for all supported data types.)

The optional **CommandLineFormat** section describes how an assessment parameter is formatted for the assessment command line. This XML node must contain a non-empty string that is a valid .NET formatting string. The assessment parameter value will be the only object that is passed to the formatter. This means that the formatting string must contain one and only one composite formatting item with index zero. Some examples are: -input {0}, /affinity:0x{0,X}, or -InputFile="{0}".

The next parameter is defined on **lines 37 - 48** and is a required parameter. The only difference in its definition from the previous parameter is an optional **Required** tag. This tag indicates that AXE expects the user to pass this parameter during AXE test execution. If this parameter is omitted, then the default value for the parameter's data type will be used (for example, zero for INT, empty string for String, etc).

Finally, the last parameter in the example specifies an optional **DefaultValue** tag, which describes the parameter's default value. If this node is blank, then the default value for the parameter's data type will be used as the default value. The example above uses "%AssessmentResultsPath%", which is an environment variable that is set by AXE when the assessment starts executing. Again, please see AXE assessment documentation for all supported AXE environment variables.

The parameters are passed to the executable in the reverse order of their definition - the parameter that is defined in the file last is passed to the executable first.

You execute the TAEF AXE [runtime parameters](runtime-parameters.md) tests as any other TAEF test that uses runtime parameters (by using the **/p** command line options):

``` syntax
te AXE.ExplicitRuntimeParameters.Examples.manifest /p:SimpleParameter=Test1 /p:RequiredParameterWithoutDefaultValue=10
Test Authoring and Execution Framework v2.7 Build 6.2.7918.0 (1320) For x64

ExplicitRuntimeParameters::ExplicitRuntimeParameters
AssessmentSample.exe is simple application for AXE assessment demo.
It just echoes the arguments passed to it to the console.

Parameters passed from the command line:
Argument[0]=AssessmentSample.exe
Argument[1]=10
Argument[2]=/RequiredParameterWithDefaultValue=C:\Results\JobResults_DEVRH_2011-0129_0250-12.394\0
Argument[3]=Test1

FileName: C:\Results\JobResults_DEVRH_2011-0129_0250-12.394\JobResults_DEVRH_2011-0129_0250-12.394.xml
Saved output file to: D:\enddev2.binaries.amd64chk\Test\CuE\TestExecution\WexLogFileOutput\
000001_~ExplicitRuntimeParameters_JobResults_DEVRH_2011-0129_0250-12.394.xml
EndGroup: ExplicitRuntimeParameters::ExplicitRuntimeParameters [Passed]

```

## <span id="AXE_Test_Cross_Machine_Execution"></span><span id="axe_test_cross_machine_execution"></span><span id="AXE_TEST_CROSS_MACHINE_EXECUTION"></span>AXE Test Cross Machine Execution


[For a cross machine execution scenario](cross-machine-execution.md), TAEF tries to determine the test dependencies that need to be deployed along with the test for successful test execution. In the case of an AXE test file, TAEF will copy all the files that are in the same folder with a TAEF AXE test to a remote machine for execution.

Cross machine execution of AXE tests to an ARM platform is not currently supported.

## <span id="TAEF_AXE_Support_Dependencies"></span><span id="taef_axe_support_dependencies"></span><span id="TAEF_AXE_SUPPORT_DEPENDENCIES"></span>TAEF AXE Support Dependencies


AXE does not ship with Windows. To be able to execute AXE tests, you need to copy **axecore.dll** and **Microsoft.Assessment.dll** to either TAEF or your TAEF AXE test directory.









