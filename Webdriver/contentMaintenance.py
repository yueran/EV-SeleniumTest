# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="yueran"
__date__ ="$May 29, 2012 12:29:26 PM$"

#global Ids:
gb_ip = "10.0.2.15"
gb_port = "8080"
gb_filename_prefix = '/home/yueran/zignage/test/EV-SeleniumTest/result'

gb_manTestValue = 6

#AddProductsToPosts:
#addProductsToPostsProduct1=u"abcd"
#addProductsToPostsProduct2=u"test product 1 Aifon"
addProductsToPostsSearchKey = u'1'
addProductsToPostsHelpLine1=u"A Media Player needs to be selected first before a product can be applied. Select a media from the Choose Media Player section."
addProductsToPostsHelpLine2=u"Once a media player is selected. Search through the Find Product section for the product to be placed on the post. Once the product is found, Click and Drag the product from the picture box and drop it in the desired post location."



#AddPostsToDisplay:

addPostsToDisplayHelpLine1 = u"In Non-touchscreen media players with multiple displays attached, this section allows posts to be assigned to specific displays."
addPostsToDisplayHelpLine2 = u"Select a device from the Choose Media Player. All DIB(s) and all Displays attached to the media player will appear. Click on the post and drag to a display that you want the product information to be displayed on."
addPostsToDisplayButtonIdentifyDisplay ="(//button[@id='identifyDisplay'])[7]"

#UploadMedia:
#
#TestMediaGroupIdValue = "78"
#TestMediaIdValue = "69"

#2)Help
uploadMediaHelpLine1 = u"Upload all types of media by clicking the Create New Media button. Media is uploaded from the local computer only."
uploadMediaHelpLine2 = u"Media Groups is an easy way to organize uploaded media."
uploadMediaHelpLine3 = u"Media removed from this area will remove the media from products or attract loops."
#3)MediaModification
#ModifyMediaGroupIdValue = "79"
uploadMediaOriginalMedia = u"MediaEditTest.avi"
uploadMediaModifiedMedia =u"MediaSuccess.avi"
#TestMediaIdValue = "69"

#Classify Products
#classifyProductsCategoryId = "70"
#classifyProductsKeywordId = "83"
#classfiyProductsSubCategoryId = "84"

#Create Products:
#1)CreateManufacture:
#createProductsManufactureId = "8"
createProductsManModifyText = u"ManTest"
createProductsManModifySuccessText=u"MModifySuccess"
createNewProduct='3testProduct'
#2)Medialist:
createProductsMedia1 ="defaultSecondaryImage.jpg"
createProductsMedia2 = "AVI_to_MPEG-4.avi"
#createProductsProduct1 = u"abcd"
##testProduct1IdValue = "95"
#createProductsProduct2 = u"xyz"
createProductsInvueProd1 = u"InvuePro1"
createProductsInvueProdKeyword ="1"
createProductsInvueProd2 = u"InvuePro2"
createProductsProdKeyword ="1"

#Assign Accessory
#testAcc1IdValue = "100"
#assignAccessoryProd1ID = "95"
#assignAccessorySearchAcc1 =u"acc1"
#assignAccessorySearchAcc2 =u"acc2"
#assignAccessoryAccSearchKey1 ="1"
#assignAccessoryCategory1 = u"test"
#assignAccessoryProSearchKey1="test"

#********************************************************
#Setup Users Or groups:
#testUserIdValue = "45"
#testUserGroupIdValue ="10"
setupUsersOrGroupsSearchUser1 = u"cd, ab"
#searchUserIdValue = "46"
setupUsersOrGroupsSearchUser2 = u"xyz, xyz"
#setupUsersOrGroupsSearchUser2ID = "47"
setupUsersOrGroupsSearchUserKey1 = "ab"
setupUsersOrGroupsSearchUserKey2 = "edit"
#assignStoreIdValue = "20"
#*create user group:
setupUsersOrGroupsNewUserGroupSendKey = "createUserGroup"
setupUsersOrGroupsNewUserGroup = u"createUserGroup"
#*Duplicate user Group:
setupUsersOrGroupsDuplicateUserGroup = u"DuplicateUserGroup"
#duplicateUserGroupIdValue = "49"
setupUsersOrGroupsDuplicateUserGroupCopySendKey = u"DuplicateSuccess"
setupUsersOrGroupsDuplicateUserGroupCopy = u"DuplicateSuccess"
#*Edit user group:
setupUsersOrGroupsEditUserGroup = u"EditUserGroup"
#editUserGroupIdValue = "51"
setupUsersOrGroupsEditUserGroupSendKey = u"EditUserGroup"
setupUsersOrGroupsEditUserGroupModifiedSendKey = "ModifiySuccess"
setupUsersOrGroupsEditUserGroupModified = "ModifiySuccess"
#*Create User:
setupUsersOrGroupsCreateUser = "lastName, firstName"
setupUsersOrGroupsCreateUserFirstName = "firstName"
setupUsersOrGroupsCreateUserFirstNameSendKeys = "firstName"
setupUsersOrGroupsCreateUserLastName = "lastName"
setupUsersOrGroupsCreateUserLastNameSendKeys = "lastName"
setupUsersOrGroupsCreateUserEmail = "lastName@firstName.com"
setupUsersOrGroupsCreateUserEmailSendKeys = "lastName@firstName.com"
setupUsersOrGroupsCreateUserUserName = "CreateUser"
setupUsersOrGroupsCreateUserUserNameSendKeys = "CreateUser"
setupUsersOrGroupsCreateUserPasswordSendKeys = "test"
setupUsersOrGroupsCreateUserRepeatPasswordSendKeys = "test"
#*Edit user:
setupUsersOrGroupsEditUser =u"editUser, editUser"
#editUserIdValue ="55"
setupUsersOrGroupsEditUserModifiedFirstNameSendKeys ="modifyUser"
setupUsersOrGroupsEditUserModifiedLastNameSendKeys ="modifyUser"
setupUsersOrGroupsEditUserModifiedEmailSendKeys ="modifyUser@test.com"
setupUsersOrGroupsEditUserModifiedUserNameSendKeys ="modifyUser"
setupUsersOrGroupsEditUserModified =u"modifyUser, modifyUser"
setupUsersOrGroupsEditUserFirstNameSendKeys ="editUser"
setupUsersOrGroupsEditUserLastNameSendKeys ="editUser"
setupUsersOrGroupsEditUserEmailSendKeys ="editUser@test.com"
setupUsersOrGroupsEditUserUserNameSendKeys ="editUser"

#********************************************************************
#storeHierarchyCompanyID = "28"
storeHierarchyCompany = u"companyTest"
#storeHierarchyStoreGroupID = "27"
storeHierarchyStoreGroup = u"storeGroupTest"
#storeHierarchyStoreID = "19"
storeHierarchyStore = u"Storetest"
storeHierarchyDuplicateStore = u"dStore"
#storeHierarchyDuplicateStoreID = "60"
storeHierarchyCompanyCopy =u"companyTest - Copy (1)"
storeHierarchyStoreGroupCopy = u"storeGroupTest - Copy (1)"
storeHierarchyDuplicateStoreCopy = u"dStore - Copy (1)"
#*edit store hierarchy:
storeHierarchyCompanyModified = u"CompanyModified"
storeHierarchyStoreGroupModified = u"StoreGroupModified"
storeHierarchyStoreModified = u"StoreModified"

#****************************************************************************
#GroupMediaPlayers:
#groupMediaPlayersDeviceStore15ID = "17"
#assignStoreIdValue = "20"
groupMediaPlayersDeviceStore15 = u"test device 1 (store 15)"
groupMediaPlayersDeviceStore16 = u"test device 1 (store 16)"
groupMediaPlayersDeviceStore15Modified = u"deviceModified"

#************************************************************************
#Template Styles:
templateStylesCreateTemp = u"CreateTmp"
templateStylesDefaultTemp = u"companyTest's Default Template"
#templateStylesDefaultTempID = "123"
templateStylesDuplicateTemp = u"DuplicateTmp"
#duplicateTmpIdValue = "225"
templateStylesDuplicateTempCopy = u"DuplicateCopyTmp"
templateStylesModifyTmp = u"ModifyTmp"
#templateStylesModifyTmpID = "227"
templateStylesTmpNameModified =u"TmpNameIsChanged"
templateStylesSearchKey = u"Modify"
#************************************************************************
#Schedule Templates:
EditTmpSchedule = u"EditTmpSchedule"
#EditTmpScheduleID ="74"
EditTmpScheduleStartDateKey1 = "10"
EditTmpScheduleStartDateKey2 = "15"
EditTmpScheduleStartDate1 = u"06/10/2012"
EditTmpScheduleStartDate2 = u"06/15/2012"
EditTmpScheduleEndDate1 = u"07/31/2012"
EditTmpScheduleEndDateKey1 = "25"
EditTmpScheduleEndDate2 = u"07/25/2012"
EditTmpScheduleEndDateKey2 = "31"
#************************************************************************
#Create Loops:
NewAttractLoop=u"zzNewAttractLoop"
DefaultAttractLoop =u"companyTest's Default Loop"
#assignLoopsIdValue="117"
assignLoops = u"assignLoops"
#assignLoopsID= "232"
#video1ID = "118"
video1 =u"AVI_to_MPEG-4.avi"
video2ID = "69"
video2 = u"ybuy attract loop.mov"
#EditNameOfLoop= u"EditNameOfLoop"
#EditAttractLoopID="233"
EditLoopNameSuccess =u"EditLoopNameSuccess"

#********************************************
#Schedule Loops:
#EditLoopSchedule=u"EditLoopSchedule"
#EditLoopScheduleID = "235"
EditLoopScheduleStartDateKey1 = "25"
EditLoopScheduleStartDateKey2 = "30"
EditLoopScheduleStartDate1 = u"06/25/2012"
EditLoopScheduleStartDate2 = u"06/30/2012"
EditLoopScheduleEndDate1 = u"07/31/2012"
EditLoopScheduleEndDateKey1 = "25"
EditLoopScheduleEndDate2 = u"07/25/2012"
EditLoopScheduleEndDateKey2 = "31"
#***************************************************
#view Network Status:
#Device1ID="17"
Device1 = u"test device 1 (store 15)"
Device2 = u"test device 1 (store 16)"
#Device2ID="18"