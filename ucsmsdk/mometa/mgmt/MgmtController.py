"""This module contains the general information for MgmtController ManagedObject."""
import sys, os

from ...ucsmo import ManagedObject
from ...ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class MgmtControllerConsts():
    DESIRED_MAINTENANCE_MODE_LPC_RESET = "lpc-reset"
    DESIRED_MAINTENANCE_MODE_NORMAL = "normal"
    DIMM_BLACKLISTING_OPER_STATE_DISABLED = "disabled"
    DIMM_BLACKLISTING_OPER_STATE_ENABLED = "enabled"
    DIMM_BLACKLISTING_OPER_STATE_UNKNOWN = "unknown"
    DIMM_BLACKLISTING_OPER_STATE_UNSUPPORTED = "unsupported"
    FSM_PREV_ACTIVATE_ADAPTOR_ACTIVATE = "ActivateAdaptorActivate"
    FSM_PREV_ACTIVATE_ADAPTOR_BEGIN = "ActivateAdaptorBegin"
    FSM_PREV_ACTIVATE_ADAPTOR_FAIL = "ActivateAdaptorFail"
    FSM_PREV_ACTIVATE_ADAPTOR_POLL_ACTIVATE_STATUS = "ActivateAdaptorPollActivateStatus"
    FSM_PREV_ACTIVATE_ADAPTOR_POWER_OFF_SERVERS = "ActivateAdaptorPowerOffServers"
    FSM_PREV_ACTIVATE_ADAPTOR_RESET = "ActivateAdaptorReset"
    FSM_PREV_ACTIVATE_ADAPTOR_SERVERS_POWER_OFF_COMPLETION = "ActivateAdaptorServersPowerOffCompletion"
    FSM_PREV_ACTIVATE_ADAPTOR_SUCCESS = "ActivateAdaptorSuccess"
    FSM_PREV_ACTIVATE_BMCACTIVATE = "ActivateBMCActivate"
    FSM_PREV_ACTIVATE_BMCBEGIN = "ActivateBMCBegin"
    FSM_PREV_ACTIVATE_BMCFAIL = "ActivateBMCFail"
    FSM_PREV_ACTIVATE_BMCRESET = "ActivateBMCReset"
    FSM_PREV_ACTIVATE_BMCSUCCESS = "ActivateBMCSuccess"
    FSM_PREV_ACTIVATE_CMCACTIVATE = "ActivateCMCActivate"
    FSM_PREV_ACTIVATE_CMCBEGIN = "ActivateCMCBegin"
    FSM_PREV_ACTIVATE_CMCFAIL = "ActivateCMCFail"
    FSM_PREV_ACTIVATE_CMCPOLL_ACTIVATION = "ActivateCMCPollActivation"
    FSM_PREV_ACTIVATE_CMCRESET = "ActivateCMCReset"
    FSM_PREV_ACTIVATE_CMCSUCCESS = "ActivateCMCSuccess"
    FSM_PREV_ACTIVATE_IOMACTIVATE = "ActivateIOMActivate"
    FSM_PREV_ACTIVATE_IOMBEGIN = "ActivateIOMBegin"
    FSM_PREV_ACTIVATE_IOMFAIL = "ActivateIOMFail"
    FSM_PREV_ACTIVATE_IOMRESET = "ActivateIOMReset"
    FSM_PREV_ACTIVATE_IOMSUCCESS = "ActivateIOMSuccess"
    FSM_PREV_EXT_MGMT_IF_CONFIG_BEGIN = "ExtMgmtIfConfigBegin"
    FSM_PREV_EXT_MGMT_IF_CONFIG_FAIL = "ExtMgmtIfConfigFail"
    FSM_PREV_EXT_MGMT_IF_CONFIG_PRIMARY = "ExtMgmtIfConfigPrimary"
    FSM_PREV_EXT_MGMT_IF_CONFIG_SECONDARY = "ExtMgmtIfConfigSecondary"
    FSM_PREV_EXT_MGMT_IF_CONFIG_SUCCESS = "ExtMgmtIfConfigSuccess"
    FSM_PREV_EXT_MGMT_INTERFACE_CONFIG_ACTIVE = "ExtMgmtInterfaceConfigActive"
    FSM_PREV_EXT_MGMT_INTERFACE_CONFIG_BEGIN = "ExtMgmtInterfaceConfigBegin"
    FSM_PREV_EXT_MGMT_INTERFACE_CONFIG_CIMCVLAN_CFG_LOCAL = "ExtMgmtInterfaceConfigCIMCVlanCfgLocal"
    FSM_PREV_EXT_MGMT_INTERFACE_CONFIG_CIMCVLAN_CFG_PEER = "ExtMgmtInterfaceConfigCIMCVlanCfgPeer"
    FSM_PREV_EXT_MGMT_INTERFACE_CONFIG_CMCVLAN_CFG = "ExtMgmtInterfaceConfigCMCVlanCfg"
    FSM_PREV_EXT_MGMT_INTERFACE_CONFIG_CMCVLAN_CFG_PEER = "ExtMgmtInterfaceConfigCMCVlanCfgPeer"
    FSM_PREV_EXT_MGMT_INTERFACE_CONFIG_FAIL = "ExtMgmtInterfaceConfigFail"
    FSM_PREV_EXT_MGMT_INTERFACE_CONFIG_SUCCESS = "ExtMgmtInterfaceConfigSuccess"
    FSM_PREV_LOCK_CONFIG_BEGIN = "LockConfigBegin"
    FSM_PREV_LOCK_CONFIG_FAIL = "LockConfigFail"
    FSM_PREV_LOCK_CONFIG_POWER_BUTTON_LOCK_CONFIG = "LockConfigPowerButtonLockConfig"
    FSM_PREV_LOCK_CONFIG_SUCCESS = "LockConfigSuccess"
    FSM_PREV_ONLINE_BEGIN = "OnlineBegin"
    FSM_PREV_ONLINE_BMC_CONFIGURE_CONN_LOCAL = "OnlineBmcConfigureConnLocal"
    FSM_PREV_ONLINE_BMC_CONFIGURE_CONN_PEER = "OnlineBmcConfigureConnPeer"
    FSM_PREV_ONLINE_FAIL = "OnlineFail"
    FSM_PREV_ONLINE_SUCCESS = "OnlineSuccess"
    FSM_PREV_ONLINE_SW_CONFIGURE_CONN_LOCAL = "OnlineSwConfigureConnLocal"
    FSM_PREV_ONLINE_SW_CONFIGURE_CONN_PEER = "OnlineSwConfigureConnPeer"
    FSM_PREV_POWER_BUDGET_RECLAIM_CONFIG_BEGIN = "PowerBudgetReclaimConfigBegin"
    FSM_PREV_POWER_BUDGET_RECLAIM_CONFIG_FAIL = "PowerBudgetReclaimConfigFail"
    FSM_PREV_POWER_BUDGET_RECLAIM_CONFIG_POWER_OFF_RECLAIM = "PowerBudgetReclaimConfigPowerOffReclaim"
    FSM_PREV_POWER_BUDGET_RECLAIM_CONFIG_POWER_OFF_WAIT = "PowerBudgetReclaimConfigPowerOffWait"
    FSM_PREV_POWER_BUDGET_RECLAIM_CONFIG_SUCCESS = "PowerBudgetReclaimConfigSuccess"
    FSM_PREV_REGISTRY_CONFIG_BEGIN = "RegistryConfigBegin"
    FSM_PREV_REGISTRY_CONFIG_FAIL = "RegistryConfigFail"
    FSM_PREV_REGISTRY_CONFIG_REMOVE = "RegistryConfigRemove"
    FSM_PREV_REGISTRY_CONFIG_SUCCESS = "RegistryConfigSuccess"
    FSM_PREV_SYS_CONFIG_BEGIN = "SysConfigBegin"
    FSM_PREV_SYS_CONFIG_FAIL = "SysConfigFail"
    FSM_PREV_SYS_CONFIG_PRIMARY = "SysConfigPrimary"
    FSM_PREV_SYS_CONFIG_SECONDARY = "SysConfigSecondary"
    FSM_PREV_SYS_CONFIG_SUCCESS = "SysConfigSuccess"
    FSM_PREV_UPDATE_ADAPTOR_BEGIN = "UpdateAdaptorBegin"
    FSM_PREV_UPDATE_ADAPTOR_FAIL = "UpdateAdaptorFail"
    FSM_PREV_UPDATE_ADAPTOR_POLL_UPDATE_STATUS = "UpdateAdaptorPollUpdateStatus"
    FSM_PREV_UPDATE_ADAPTOR_SUCCESS = "UpdateAdaptorSuccess"
    FSM_PREV_UPDATE_ADAPTOR_UPDATE_REQUEST = "UpdateAdaptorUpdateRequest"
    FSM_PREV_UPDATE_BMCBEGIN = "UpdateBMCBegin"
    FSM_PREV_UPDATE_BMCFAIL = "UpdateBMCFail"
    FSM_PREV_UPDATE_BMCPOLL_UPDATE_STATUS = "UpdateBMCPollUpdateStatus"
    FSM_PREV_UPDATE_BMCSUCCESS = "UpdateBMCSuccess"
    FSM_PREV_UPDATE_BMCUPDATE_REQUEST = "UpdateBMCUpdateRequest"
    FSM_PREV_UPDATE_BOARD_CONTROLLER_BEGIN = "UpdateBoardControllerBegin"
    FSM_PREV_UPDATE_BOARD_CONTROLLER_FAIL = "UpdateBoardControllerFail"
    FSM_PREV_UPDATE_BOARD_CONTROLLER_POLL_UPDATE_STATUS = "UpdateBoardControllerPollUpdateStatus"
    FSM_PREV_UPDATE_BOARD_CONTROLLER_POWER_OFF_SERVERS = "UpdateBoardControllerPowerOffServers"
    FSM_PREV_UPDATE_BOARD_CONTROLLER_PREPARE_FOR_UPDATE = "UpdateBoardControllerPrepareForUpdate"
    FSM_PREV_UPDATE_BOARD_CONTROLLER_SERVERS_POWER_OFF_COMPLETION = "UpdateBoardControllerServersPowerOffCompletion"
    FSM_PREV_UPDATE_BOARD_CONTROLLER_SUCCESS = "UpdateBoardControllerSuccess"
    FSM_PREV_UPDATE_BOARD_CONTROLLER_UPDATE_REQUEST = "UpdateBoardControllerUpdateRequest"
    FSM_PREV_UPDATE_CMCBEGIN = "UpdateCMCBegin"
    FSM_PREV_UPDATE_CMCFAIL = "UpdateCMCFail"
    FSM_PREV_UPDATE_CMCPOLL_UPDATE_STATUS = "UpdateCMCPollUpdateStatus"
    FSM_PREV_UPDATE_CMCSUCCESS = "UpdateCMCSuccess"
    FSM_PREV_UPDATE_CMCUPDATE_REQUEST = "UpdateCMCUpdateRequest"
    FSM_PREV_UPDATE_IOMBEGIN = "UpdateIOMBegin"
    FSM_PREV_UPDATE_IOMCOPY_IOMIMG_TO_SUB = "UpdateIOMCopyIOMImgToSub"
    FSM_PREV_UPDATE_IOMCOPY_IMG_FROM_REP = "UpdateIOMCopyImgFromRep"
    FSM_PREV_UPDATE_IOMFAIL = "UpdateIOMFail"
    FSM_PREV_UPDATE_IOMPOLL_UPDATE_STATUS = "UpdateIOMPollUpdateStatus"
    FSM_PREV_UPDATE_IOMSUCCESS = "UpdateIOMSuccess"
    FSM_PREV_UPDATE_IOMUPDATE_REQUEST = "UpdateIOMUpdateRequest"
    FSM_PREV_UPDATE_RAID_CONTROLLER_ACTIVATE = "UpdateRaidControllerActivate"
    FSM_PREV_UPDATE_RAID_CONTROLLER_BEGIN = "UpdateRaidControllerBegin"
    FSM_PREV_UPDATE_RAID_CONTROLLER_FAIL = "UpdateRaidControllerFail"
    FSM_PREV_UPDATE_RAID_CONTROLLER_POLL_ACTIVATION = "UpdateRaidControllerPollActivation"
    FSM_PREV_UPDATE_RAID_CONTROLLER_POLL_UPDATE_STATUS = "UpdateRaidControllerPollUpdateStatus"
    FSM_PREV_UPDATE_RAID_CONTROLLER_POWER_OFF_SERVERS = "UpdateRaidControllerPowerOffServers"
    FSM_PREV_UPDATE_RAID_CONTROLLER_SERVERS_POWER_OFF_COMPLETION = "UpdateRaidControllerServersPowerOffCompletion"
    FSM_PREV_UPDATE_RAID_CONTROLLER_SUCCESS = "UpdateRaidControllerSuccess"
    FSM_PREV_UPDATE_RAID_CONTROLLER_UPDATE_REQUEST = "UpdateRaidControllerUpdateRequest"
    FSM_PREV_UPDATE_SWITCH_BEGIN = "UpdateSwitchBegin"
    FSM_PREV_UPDATE_SWITCH_COPY_TO_LOCAL = "UpdateSwitchCopyToLocal"
    FSM_PREV_UPDATE_SWITCH_COPY_TO_PEER = "UpdateSwitchCopyToPeer"
    FSM_PREV_UPDATE_SWITCH_FAIL = "UpdateSwitchFail"
    FSM_PREV_UPDATE_SWITCH_RESET_LOCAL = "UpdateSwitchResetLocal"
    FSM_PREV_UPDATE_SWITCH_RESET_REMOTE = "UpdateSwitchResetRemote"
    FSM_PREV_UPDATE_SWITCH_SUCCESS = "UpdateSwitchSuccess"
    FSM_PREV_UPDATE_SWITCH_UPDATE_LOCAL = "UpdateSwitchUpdateLocal"
    FSM_PREV_UPDATE_SWITCH_UPDATE_REMOTE = "UpdateSwitchUpdateRemote"
    FSM_PREV_UPDATE_SWITCH_VERIFY_LOCAL = "UpdateSwitchVerifyLocal"
    FSM_PREV_UPDATE_SWITCH_VERIFY_REMOTE = "UpdateSwitchVerifyRemote"
    FSM_PREV_UPDATE_UCSMANAGER_BEGIN = "UpdateUCSManagerBegin"
    FSM_PREV_UPDATE_UCSMANAGER_COPY_EXT_TO_LOCAL = "UpdateUCSManagerCopyExtToLocal"
    FSM_PREV_UPDATE_UCSMANAGER_COPY_EXT_TO_PEER = "UpdateUCSManagerCopyExtToPeer"
    FSM_PREV_UPDATE_UCSMANAGER_EXECUTE = "UpdateUCSManagerExecute"
    FSM_PREV_UPDATE_UCSMANAGER_FAIL = "UpdateUCSManagerFail"
    FSM_PREV_UPDATE_UCSMANAGER_START = "UpdateUCSManagerStart"
    FSM_PREV_UPDATE_UCSMANAGER_SUCCESS = "UpdateUCSManagerSuccess"
    FSM_PREV_NOP = "nop"
    FSM_RMT_INV_ERR_CODE_ERR_2FA_AUTH_RETRY = "ERR-2fa-auth-retry"
    FSM_RMT_INV_ERR_CODE_ERR_ACTIVATE_FAILED = "ERR-ACTIVATE-failed"
    FSM_RMT_INV_ERR_CODE_ERR_ACTIVATE_IN_PROGRESS = "ERR-ACTIVATE-in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_ACTIVATE_RETRY = "ERR-ACTIVATE-retry"
    FSM_RMT_INV_ERR_CODE_ERR_BIOS_TOKENS_OLD_BIOS = "ERR-BIOS-TOKENS-OLD-BIOS"
    FSM_RMT_INV_ERR_CODE_ERR_BIOS_TOKENS_OLD_CIMC = "ERR-BIOS-TOKENS-OLD-CIMC"
    FSM_RMT_INV_ERR_CODE_ERR_BIOS_NETWORK_BOOT_ORDER_NOT_FOUND = "ERR-BIOS-network-boot-order-not-found"
    FSM_RMT_INV_ERR_CODE_ERR_BOARDCTRLUPDATE_IGNORE = "ERR-BOARDCTRLUPDATE-ignore"
    FSM_RMT_INV_ERR_CODE_ERR_DIAG_CANCELLED = "ERR-DIAG-cancelled"
    FSM_RMT_INV_ERR_CODE_ERR_DIAG_FSM_RESTARTED = "ERR-DIAG-fsm-restarted"
    FSM_RMT_INV_ERR_CODE_ERR_DIAG_TEST_FAILED = "ERR-DIAG-test-failed"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_AUTHENTICATION_FAILURE = "ERR-DNLD-authentication-failure"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_HOSTKEY_MISMATCH = "ERR-DNLD-hostkey-mismatch"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_INVALID_IMAGE = "ERR-DNLD-invalid-image"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_NO_FILE = "ERR-DNLD-no-file"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_NO_SPACE = "ERR-DNLD-no-space"
    FSM_RMT_INV_ERR_CODE_ERR_DNLD_USB_UNMOUNTED = "ERR-DNLD-usb-unmounted"
    FSM_RMT_INV_ERR_CODE_ERR_DNS_DELETE_ERROR = "ERR-DNS-delete-error"
    FSM_RMT_INV_ERR_CODE_ERR_DNS_GET_ERROR = "ERR-DNS-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_DNS_SET_ERROR = "ERR-DNS-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_DIAGNOSTICS_IN_PROGRESS = "ERR-Diagnostics-in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_DIAGNOSTICS_MEMTEST_IN_PROGRESS = "ERR-Diagnostics-memtest-in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_DIAGNOSTICS_NETWORK_IN_PROGRESS = "ERR-Diagnostics-network-in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_FILTER_ILLEGAL_FORMAT = "ERR-FILTER-illegal-format"
    FSM_RMT_INV_ERR_CODE_ERR_FSM_NO_SUCH_STATE = "ERR-FSM-no-such-state"
    FSM_RMT_INV_ERR_CODE_ERR_HOST_FRU_IDENTITY_MISMATCH = "ERR-HOST-fru-identity-mismatch"
    FSM_RMT_INV_ERR_CODE_ERR_HTTP_SET_ERROR = "ERR-HTTP-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_HTTPS_SET_ERROR = "ERR-HTTPS-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_IBMC_ANALYZE_RESULTS = "ERR-IBMC-analyze-results"
    FSM_RMT_INV_ERR_CODE_ERR_IBMC_CONNECT_ERROR = "ERR-IBMC-connect-error"
    FSM_RMT_INV_ERR_CODE_ERR_IBMC_CONNECTOR_INFO_RETRIEVAL_ERROR = "ERR-IBMC-connector-info-retrieval-error"
    FSM_RMT_INV_ERR_CODE_ERR_IBMC_FRU_RETRIEVAL_ERROR = "ERR-IBMC-fru-retrieval-error"
    FSM_RMT_INV_ERR_CODE_ERR_IBMC_INVALID_END_POINT_CONFIG = "ERR-IBMC-invalid-end-point-config"
    FSM_RMT_INV_ERR_CODE_ERR_IBMC_RESULTS_NOT_READY = "ERR-IBMC-results-not-ready"
    FSM_RMT_INV_ERR_CODE_ERR_MAX_SUBSCRIPTIONS_ALLOWED_ERROR = "ERR-MAX-subscriptions-allowed-error"
    FSM_RMT_INV_ERR_CODE_ERR_MO_CONFIG_CHILD_OBJECT_CANT_BE_CONFIGURED = "ERR-MO-CONFIG-child-object-cant-be-configured"
    FSM_RMT_INV_ERR_CODE_ERR_MO_META_NO_SUCH_OBJECT_CLASS = "ERR-MO-META-no-such-object-class"
    FSM_RMT_INV_ERR_CODE_ERR_MO_PROPERTY_NO_SUCH_PROPERTY = "ERR-MO-PROPERTY-no-such-property"
    FSM_RMT_INV_ERR_CODE_ERR_MO_PROPERTY_VALUE_OUT_OF_RANGE = "ERR-MO-PROPERTY-value-out-of-range"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ACCESS_DENIED = "ERR-MO-access-denied"
    FSM_RMT_INV_ERR_CODE_ERR_MO_DELETION_RULE_VIOLATION = "ERR-MO-deletion-rule-violation"
    FSM_RMT_INV_ERR_CODE_ERR_MO_DUPLICATE_OBJECT = "ERR-MO-duplicate-object"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_CONTAINMENT = "ERR-MO-illegal-containment"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_CREATION = "ERR-MO-illegal-creation"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_ITERATOR_STATE = "ERR-MO-illegal-iterator-state"
    FSM_RMT_INV_ERR_CODE_ERR_MO_ILLEGAL_OBJECT_LIFECYCLE_TRANSITION = "ERR-MO-illegal-object-lifecycle-transition"
    FSM_RMT_INV_ERR_CODE_ERR_MO_NAMING_RULE_VIOLATION = "ERR-MO-naming-rule-violation"
    FSM_RMT_INV_ERR_CODE_ERR_MO_OBJECT_NOT_FOUND = "ERR-MO-object-not-found"
    FSM_RMT_INV_ERR_CODE_ERR_MO_RESOURCE_ALLOCATION = "ERR-MO-resource-allocation"
    FSM_RMT_INV_ERR_CODE_ERR_NTP_DELETE_ERROR = "ERR-NTP-delete-error"
    FSM_RMT_INV_ERR_CODE_ERR_NTP_GET_ERROR = "ERR-NTP-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_NTP_SET_ERROR = "ERR-NTP-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_POWER_CAP_UNSUPPORTED = "ERR-POWER-CAP-UNSUPPORTED"
    FSM_RMT_INV_ERR_CODE_ERR_POWER_PROFILE_IN_PROGRESS = "ERR-POWER-PROFILE-IN-PROGRESS"
    FSM_RMT_INV_ERR_CODE_ERR_SERVER_MIS_CONNECT = "ERR-SERVER-mis-connect"
    FSM_RMT_INV_ERR_CODE_ERR_SWITCH_INVALID_IF_CONFIG = "ERR-SWITCH-invalid-if-config"
    FSM_RMT_INV_ERR_CODE_ERR_TOKEN_REQUEST_DENIED = "ERR-TOKEN-request-denied"
    FSM_RMT_INV_ERR_CODE_ERR_UNABLE_TO_FETCH_BIOS_SETTINGS = "ERR-UNABLE-TO-FETCH-BIOS-SETTINGS"
    FSM_RMT_INV_ERR_CODE_ERR_UPDATE_FAILED = "ERR-UPDATE-failed"
    FSM_RMT_INV_ERR_CODE_ERR_UPDATE_IN_PROGRESS = "ERR-UPDATE-in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_UPDATE_RETRY = "ERR-UPDATE-retry"
    FSM_RMT_INV_ERR_CODE_ERR_AAA_CONFIG_MODIFY_ERROR = "ERR-aaa-config-modify-error"
    FSM_RMT_INV_ERR_CODE_ERR_ACCT_REALM_SET_ERROR = "ERR-acct-realm-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_ADMIN_PASSWD_SET = "ERR-admin-passwd-set"
    FSM_RMT_INV_ERR_CODE_ERR_AUTH_ISSUE = "ERR-auth-issue"
    FSM_RMT_INV_ERR_CODE_ERR_AUTH_REALM_GET_ERROR = "ERR-auth-realm-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_AUTH_REALM_SET_ERROR = "ERR-auth-realm-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_AUTHENTICATION = "ERR-authentication"
    FSM_RMT_INV_ERR_CODE_ERR_AUTHORIZATION_REQUIRED = "ERR-authorization-required"
    FSM_RMT_INV_ERR_CODE_ERR_CLI_SESSION_LIMIT_REACHED = "ERR-cli-session-limit-reached"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_KEYRING = "ERR-create-keyring"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_LOCALE = "ERR-create-locale"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_ROLE = "ERR-create-role"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_TP = "ERR-create-tp"
    FSM_RMT_INV_ERR_CODE_ERR_CREATE_USER = "ERR-create-user"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_LOCALE = "ERR-delete-locale"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_ROLE = "ERR-delete-role"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_SESSION = "ERR-delete-session"
    FSM_RMT_INV_ERR_CODE_ERR_DELETE_USER = "ERR-delete-user"
    FSM_RMT_INV_ERR_CODE_ERR_DOWNGRADE_FAIL = "ERR-downgrade-fail"
    FSM_RMT_INV_ERR_CODE_ERR_EFI_DIAGNOSTICS_IN_PROGRESS = "ERR-efi-Diagnostics--in-progress"
    FSM_RMT_INV_ERR_CODE_ERR_ENABLE_MGMT_CONN = "ERR-enable-mgmt-conn"
    FSM_RMT_INV_ERR_CODE_ERR_EP_SET_ERROR = "ERR-ep-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_GET_MAX_HTTP_USER_SESSIONS = "ERR-get-max-http-user-sessions"
    FSM_RMT_INV_ERR_CODE_ERR_HTTP_INITIALIZING = "ERR-http-initializing"
    FSM_RMT_INV_ERR_CODE_ERR_INSUFFICIENTLY_EQUIPPED = "ERR-insufficiently-equipped"
    FSM_RMT_INV_ERR_CODE_ERR_INTERNAL_ERROR = "ERR-internal-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_DELETE_ERROR = "ERR-ldap-delete-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_GET_ERROR = "ERR-ldap-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_GROUP_MODIFY_ERROR = "ERR-ldap-group-modify-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_GROUP_SET_ERROR = "ERR-ldap-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_LDAP_SET_ERROR = "ERR-ldap-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_LOCALE_SET_ERROR = "ERR-locale-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_MAX_USERID_SESSIONS_REACHED = "ERR-max-userid-sessions-reached"
    FSM_RMT_INV_ERR_CODE_ERR_MISSING_METHOD = "ERR-missing-method"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_LOCALE = "ERR-modify-locale"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_ROLE = "ERR-modify-role"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_USER = "ERR-modify-user"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_USER_LOCALE = "ERR-modify-user-locale"
    FSM_RMT_INV_ERR_CODE_ERR_MODIFY_USER_ROLE = "ERR-modify-user-role"
    FSM_RMT_INV_ERR_CODE_ERR_PROVIDER_GROUP_MODIFY_ERROR = "ERR-provider-group-modify-error"
    FSM_RMT_INV_ERR_CODE_ERR_PROVIDER_GROUP_SET_ERROR = "ERR-provider-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_GET_ERROR = "ERR-radius-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_GLOBAL_SET_ERROR = "ERR-radius-global-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_GROUP_SET_ERROR = "ERR-radius-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_RADIUS_SET_ERROR = "ERR-radius-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_REQUEST_TIMEOUT = "ERR-request-timeout"
    FSM_RMT_INV_ERR_CODE_ERR_RESET_ADAPTER = "ERR-reset-adapter"
    FSM_RMT_INV_ERR_CODE_ERR_ROLE_SET_ERROR = "ERR-role-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_SECONDARY_NODE = "ERR-secondary-node"
    FSM_RMT_INV_ERR_CODE_ERR_SERVICE_NOT_READY = "ERR-service-not-ready"
    FSM_RMT_INV_ERR_CODE_ERR_SESSION_CACHE_FULL = "ERR-session-cache-full"
    FSM_RMT_INV_ERR_CODE_ERR_SESSION_NOT_FOUND = "ERR-session-not-found"
    FSM_RMT_INV_ERR_CODE_ERR_SET_NETWORK = "ERR-set-network"
    FSM_RMT_INV_ERR_CODE_ERR_SET_PASSWORD_STRENGTH_CHECK = "ERR-set-password-strength-check"
    FSM_RMT_INV_ERR_CODE_ERR_SET_PORT_CHANNEL = "ERR-set-port-channel"
    FSM_RMT_INV_ERR_CODE_ERR_STORE_PRE_LOGIN_BANNER_MSG = "ERR-store-pre-login-banner-msg"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_ENABLE_ERROR = "ERR-tacacs-enable-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_GLOBAL_SET_ERROR = "ERR-tacacs-global-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_GROUP_SET_ERROR = "ERR-tacacs-group-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_PLUS_GET_ERROR = "ERR-tacacs-plus-get-error"
    FSM_RMT_INV_ERR_CODE_ERR_TACACS_SET_ERROR = "ERR-tacacs-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_TEST_ERROR_1 = "ERR-test-error-1"
    FSM_RMT_INV_ERR_CODE_ERR_TEST_ERROR_2 = "ERR-test-error-2"
    FSM_RMT_INV_ERR_CODE_ERR_TIMEZONE_SET_ERROR = "ERR-timezone-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_USER_ACCOUNT_EXPIRED = "ERR-user-account-expired"
    FSM_RMT_INV_ERR_CODE_ERR_USER_SET_ERROR = "ERR-user-set-error"
    FSM_RMT_INV_ERR_CODE_ERR_XML_PARSE_ERROR = "ERR-xml-parse-error"
    FSM_RMT_INV_ERR_CODE_NONE = "none"
    FSM_STAMP_NEVER = "never"
    FSM_STATUS_ACTIVATE_ADAPTOR_ACTIVATE = "ActivateAdaptorActivate"
    FSM_STATUS_ACTIVATE_ADAPTOR_BEGIN = "ActivateAdaptorBegin"
    FSM_STATUS_ACTIVATE_ADAPTOR_FAIL = "ActivateAdaptorFail"
    FSM_STATUS_ACTIVATE_ADAPTOR_POLL_ACTIVATE_STATUS = "ActivateAdaptorPollActivateStatus"
    FSM_STATUS_ACTIVATE_ADAPTOR_POWER_OFF_SERVERS = "ActivateAdaptorPowerOffServers"
    FSM_STATUS_ACTIVATE_ADAPTOR_RESET = "ActivateAdaptorReset"
    FSM_STATUS_ACTIVATE_ADAPTOR_SERVERS_POWER_OFF_COMPLETION = "ActivateAdaptorServersPowerOffCompletion"
    FSM_STATUS_ACTIVATE_ADAPTOR_SUCCESS = "ActivateAdaptorSuccess"
    FSM_STATUS_ACTIVATE_BMCACTIVATE = "ActivateBMCActivate"
    FSM_STATUS_ACTIVATE_BMCBEGIN = "ActivateBMCBegin"
    FSM_STATUS_ACTIVATE_BMCFAIL = "ActivateBMCFail"
    FSM_STATUS_ACTIVATE_BMCRESET = "ActivateBMCReset"
    FSM_STATUS_ACTIVATE_BMCSUCCESS = "ActivateBMCSuccess"
    FSM_STATUS_ACTIVATE_CMCACTIVATE = "ActivateCMCActivate"
    FSM_STATUS_ACTIVATE_CMCBEGIN = "ActivateCMCBegin"
    FSM_STATUS_ACTIVATE_CMCFAIL = "ActivateCMCFail"
    FSM_STATUS_ACTIVATE_CMCPOLL_ACTIVATION = "ActivateCMCPollActivation"
    FSM_STATUS_ACTIVATE_CMCRESET = "ActivateCMCReset"
    FSM_STATUS_ACTIVATE_CMCSUCCESS = "ActivateCMCSuccess"
    FSM_STATUS_ACTIVATE_IOMACTIVATE = "ActivateIOMActivate"
    FSM_STATUS_ACTIVATE_IOMBEGIN = "ActivateIOMBegin"
    FSM_STATUS_ACTIVATE_IOMFAIL = "ActivateIOMFail"
    FSM_STATUS_ACTIVATE_IOMRESET = "ActivateIOMReset"
    FSM_STATUS_ACTIVATE_IOMSUCCESS = "ActivateIOMSuccess"
    FSM_STATUS_EXT_MGMT_IF_CONFIG_BEGIN = "ExtMgmtIfConfigBegin"
    FSM_STATUS_EXT_MGMT_IF_CONFIG_FAIL = "ExtMgmtIfConfigFail"
    FSM_STATUS_EXT_MGMT_IF_CONFIG_PRIMARY = "ExtMgmtIfConfigPrimary"
    FSM_STATUS_EXT_MGMT_IF_CONFIG_SECONDARY = "ExtMgmtIfConfigSecondary"
    FSM_STATUS_EXT_MGMT_IF_CONFIG_SUCCESS = "ExtMgmtIfConfigSuccess"
    FSM_STATUS_EXT_MGMT_INTERFACE_CONFIG_ACTIVE = "ExtMgmtInterfaceConfigActive"
    FSM_STATUS_EXT_MGMT_INTERFACE_CONFIG_BEGIN = "ExtMgmtInterfaceConfigBegin"
    FSM_STATUS_EXT_MGMT_INTERFACE_CONFIG_CIMCVLAN_CFG_LOCAL = "ExtMgmtInterfaceConfigCIMCVlanCfgLocal"
    FSM_STATUS_EXT_MGMT_INTERFACE_CONFIG_CIMCVLAN_CFG_PEER = "ExtMgmtInterfaceConfigCIMCVlanCfgPeer"
    FSM_STATUS_EXT_MGMT_INTERFACE_CONFIG_CMCVLAN_CFG = "ExtMgmtInterfaceConfigCMCVlanCfg"
    FSM_STATUS_EXT_MGMT_INTERFACE_CONFIG_CMCVLAN_CFG_PEER = "ExtMgmtInterfaceConfigCMCVlanCfgPeer"
    FSM_STATUS_EXT_MGMT_INTERFACE_CONFIG_FAIL = "ExtMgmtInterfaceConfigFail"
    FSM_STATUS_EXT_MGMT_INTERFACE_CONFIG_SUCCESS = "ExtMgmtInterfaceConfigSuccess"
    FSM_STATUS_LOCK_CONFIG_BEGIN = "LockConfigBegin"
    FSM_STATUS_LOCK_CONFIG_FAIL = "LockConfigFail"
    FSM_STATUS_LOCK_CONFIG_POWER_BUTTON_LOCK_CONFIG = "LockConfigPowerButtonLockConfig"
    FSM_STATUS_LOCK_CONFIG_SUCCESS = "LockConfigSuccess"
    FSM_STATUS_ONLINE_BEGIN = "OnlineBegin"
    FSM_STATUS_ONLINE_BMC_CONFIGURE_CONN_LOCAL = "OnlineBmcConfigureConnLocal"
    FSM_STATUS_ONLINE_BMC_CONFIGURE_CONN_PEER = "OnlineBmcConfigureConnPeer"
    FSM_STATUS_ONLINE_FAIL = "OnlineFail"
    FSM_STATUS_ONLINE_SUCCESS = "OnlineSuccess"
    FSM_STATUS_ONLINE_SW_CONFIGURE_CONN_LOCAL = "OnlineSwConfigureConnLocal"
    FSM_STATUS_ONLINE_SW_CONFIGURE_CONN_PEER = "OnlineSwConfigureConnPeer"
    FSM_STATUS_POWER_BUDGET_RECLAIM_CONFIG_BEGIN = "PowerBudgetReclaimConfigBegin"
    FSM_STATUS_POWER_BUDGET_RECLAIM_CONFIG_FAIL = "PowerBudgetReclaimConfigFail"
    FSM_STATUS_POWER_BUDGET_RECLAIM_CONFIG_POWER_OFF_RECLAIM = "PowerBudgetReclaimConfigPowerOffReclaim"
    FSM_STATUS_POWER_BUDGET_RECLAIM_CONFIG_POWER_OFF_WAIT = "PowerBudgetReclaimConfigPowerOffWait"
    FSM_STATUS_POWER_BUDGET_RECLAIM_CONFIG_SUCCESS = "PowerBudgetReclaimConfigSuccess"
    FSM_STATUS_REGISTRY_CONFIG_BEGIN = "RegistryConfigBegin"
    FSM_STATUS_REGISTRY_CONFIG_FAIL = "RegistryConfigFail"
    FSM_STATUS_REGISTRY_CONFIG_REMOVE = "RegistryConfigRemove"
    FSM_STATUS_REGISTRY_CONFIG_SUCCESS = "RegistryConfigSuccess"
    FSM_STATUS_SYS_CONFIG_BEGIN = "SysConfigBegin"
    FSM_STATUS_SYS_CONFIG_FAIL = "SysConfigFail"
    FSM_STATUS_SYS_CONFIG_PRIMARY = "SysConfigPrimary"
    FSM_STATUS_SYS_CONFIG_SECONDARY = "SysConfigSecondary"
    FSM_STATUS_SYS_CONFIG_SUCCESS = "SysConfigSuccess"
    FSM_STATUS_UPDATE_ADAPTOR_BEGIN = "UpdateAdaptorBegin"
    FSM_STATUS_UPDATE_ADAPTOR_FAIL = "UpdateAdaptorFail"
    FSM_STATUS_UPDATE_ADAPTOR_POLL_UPDATE_STATUS = "UpdateAdaptorPollUpdateStatus"
    FSM_STATUS_UPDATE_ADAPTOR_SUCCESS = "UpdateAdaptorSuccess"
    FSM_STATUS_UPDATE_ADAPTOR_UPDATE_REQUEST = "UpdateAdaptorUpdateRequest"
    FSM_STATUS_UPDATE_BMCBEGIN = "UpdateBMCBegin"
    FSM_STATUS_UPDATE_BMCFAIL = "UpdateBMCFail"
    FSM_STATUS_UPDATE_BMCPOLL_UPDATE_STATUS = "UpdateBMCPollUpdateStatus"
    FSM_STATUS_UPDATE_BMCSUCCESS = "UpdateBMCSuccess"
    FSM_STATUS_UPDATE_BMCUPDATE_REQUEST = "UpdateBMCUpdateRequest"
    FSM_STATUS_UPDATE_BOARD_CONTROLLER_BEGIN = "UpdateBoardControllerBegin"
    FSM_STATUS_UPDATE_BOARD_CONTROLLER_FAIL = "UpdateBoardControllerFail"
    FSM_STATUS_UPDATE_BOARD_CONTROLLER_POLL_UPDATE_STATUS = "UpdateBoardControllerPollUpdateStatus"
    FSM_STATUS_UPDATE_BOARD_CONTROLLER_POWER_OFF_SERVERS = "UpdateBoardControllerPowerOffServers"
    FSM_STATUS_UPDATE_BOARD_CONTROLLER_PREPARE_FOR_UPDATE = "UpdateBoardControllerPrepareForUpdate"
    FSM_STATUS_UPDATE_BOARD_CONTROLLER_SERVERS_POWER_OFF_COMPLETION = "UpdateBoardControllerServersPowerOffCompletion"
    FSM_STATUS_UPDATE_BOARD_CONTROLLER_SUCCESS = "UpdateBoardControllerSuccess"
    FSM_STATUS_UPDATE_BOARD_CONTROLLER_UPDATE_REQUEST = "UpdateBoardControllerUpdateRequest"
    FSM_STATUS_UPDATE_CMCBEGIN = "UpdateCMCBegin"
    FSM_STATUS_UPDATE_CMCFAIL = "UpdateCMCFail"
    FSM_STATUS_UPDATE_CMCPOLL_UPDATE_STATUS = "UpdateCMCPollUpdateStatus"
    FSM_STATUS_UPDATE_CMCSUCCESS = "UpdateCMCSuccess"
    FSM_STATUS_UPDATE_CMCUPDATE_REQUEST = "UpdateCMCUpdateRequest"
    FSM_STATUS_UPDATE_IOMBEGIN = "UpdateIOMBegin"
    FSM_STATUS_UPDATE_IOMCOPY_IOMIMG_TO_SUB = "UpdateIOMCopyIOMImgToSub"
    FSM_STATUS_UPDATE_IOMCOPY_IMG_FROM_REP = "UpdateIOMCopyImgFromRep"
    FSM_STATUS_UPDATE_IOMFAIL = "UpdateIOMFail"
    FSM_STATUS_UPDATE_IOMPOLL_UPDATE_STATUS = "UpdateIOMPollUpdateStatus"
    FSM_STATUS_UPDATE_IOMSUCCESS = "UpdateIOMSuccess"
    FSM_STATUS_UPDATE_IOMUPDATE_REQUEST = "UpdateIOMUpdateRequest"
    FSM_STATUS_UPDATE_RAID_CONTROLLER_ACTIVATE = "UpdateRaidControllerActivate"
    FSM_STATUS_UPDATE_RAID_CONTROLLER_BEGIN = "UpdateRaidControllerBegin"
    FSM_STATUS_UPDATE_RAID_CONTROLLER_FAIL = "UpdateRaidControllerFail"
    FSM_STATUS_UPDATE_RAID_CONTROLLER_POLL_ACTIVATION = "UpdateRaidControllerPollActivation"
    FSM_STATUS_UPDATE_RAID_CONTROLLER_POLL_UPDATE_STATUS = "UpdateRaidControllerPollUpdateStatus"
    FSM_STATUS_UPDATE_RAID_CONTROLLER_POWER_OFF_SERVERS = "UpdateRaidControllerPowerOffServers"
    FSM_STATUS_UPDATE_RAID_CONTROLLER_SERVERS_POWER_OFF_COMPLETION = "UpdateRaidControllerServersPowerOffCompletion"
    FSM_STATUS_UPDATE_RAID_CONTROLLER_SUCCESS = "UpdateRaidControllerSuccess"
    FSM_STATUS_UPDATE_RAID_CONTROLLER_UPDATE_REQUEST = "UpdateRaidControllerUpdateRequest"
    FSM_STATUS_UPDATE_SWITCH_BEGIN = "UpdateSwitchBegin"
    FSM_STATUS_UPDATE_SWITCH_COPY_TO_LOCAL = "UpdateSwitchCopyToLocal"
    FSM_STATUS_UPDATE_SWITCH_COPY_TO_PEER = "UpdateSwitchCopyToPeer"
    FSM_STATUS_UPDATE_SWITCH_FAIL = "UpdateSwitchFail"
    FSM_STATUS_UPDATE_SWITCH_RESET_LOCAL = "UpdateSwitchResetLocal"
    FSM_STATUS_UPDATE_SWITCH_RESET_REMOTE = "UpdateSwitchResetRemote"
    FSM_STATUS_UPDATE_SWITCH_SUCCESS = "UpdateSwitchSuccess"
    FSM_STATUS_UPDATE_SWITCH_UPDATE_LOCAL = "UpdateSwitchUpdateLocal"
    FSM_STATUS_UPDATE_SWITCH_UPDATE_REMOTE = "UpdateSwitchUpdateRemote"
    FSM_STATUS_UPDATE_SWITCH_VERIFY_LOCAL = "UpdateSwitchVerifyLocal"
    FSM_STATUS_UPDATE_SWITCH_VERIFY_REMOTE = "UpdateSwitchVerifyRemote"
    FSM_STATUS_UPDATE_UCSMANAGER_BEGIN = "UpdateUCSManagerBegin"
    FSM_STATUS_UPDATE_UCSMANAGER_COPY_EXT_TO_LOCAL = "UpdateUCSManagerCopyExtToLocal"
    FSM_STATUS_UPDATE_UCSMANAGER_COPY_EXT_TO_PEER = "UpdateUCSManagerCopyExtToPeer"
    FSM_STATUS_UPDATE_UCSMANAGER_EXECUTE = "UpdateUCSManagerExecute"
    FSM_STATUS_UPDATE_UCSMANAGER_FAIL = "UpdateUCSManagerFail"
    FSM_STATUS_UPDATE_UCSMANAGER_START = "UpdateUCSManagerStart"
    FSM_STATUS_UPDATE_UCSMANAGER_SUCCESS = "UpdateUCSManagerSuccess"
    FSM_STATUS_NOP = "nop"
    ID_A = "A"
    ID_B = "B"
    ID_NONE = "NONE"
    POWER_FAN_SPEED_POLICY_SUPPORTED_FALSE = "false"
    POWER_FAN_SPEED_POLICY_SUPPORTED_NO = "no"
    POWER_FAN_SPEED_POLICY_SUPPORTED_TRUE = "true"
    POWER_FAN_SPEED_POLICY_SUPPORTED_YES = "yes"
    STORAGE_OOB_CONFIG_SUPPORTED_FALSE = "false"
    STORAGE_OOB_CONFIG_SUPPORTED_NO = "no"
    STORAGE_OOB_CONFIG_SUPPORTED_TRUE = "true"
    STORAGE_OOB_CONFIG_SUPPORTED_YES = "yes"
    STORAGE_OOB_INTERFACE_SUPPORTED_FALSE = "false"
    STORAGE_OOB_INTERFACE_SUPPORTED_NO = "no"
    STORAGE_OOB_INTERFACE_SUPPORTED_TRUE = "true"
    STORAGE_OOB_INTERFACE_SUPPORTED_YES = "yes"
    STORAGE_SUBSYSTEM_STATE_INITIALIZED = "initialized"
    STORAGE_SUBSYSTEM_STATE_INITIALIZING = "initializing"
    STORAGE_SUBSYSTEM_STATE_UNINITIALIZED = "uninitialized"
    STORAGE_SUBSYSTEM_STATE_UNKNOWN = "unknown"
    STORAGE_SUBSYSTEM_STATE_UNSUPPORTED = "unsupported"
    SUBJECT_ADAPTOR = "adaptor"
    SUBJECT_BLADE = "blade"
    SUBJECT_BOARD_CONTROLLER = "board-controller"
    SUBJECT_CHASSIS = "chassis"
    SUBJECT_CMC = "cmc"
    SUBJECT_IOCARD = "iocard"
    SUBJECT_SERVER_UNIT = "server-unit"
    SUBJECT_SWITCH = "switch"
    SUBJECT_SYSTEM = "system"
    SUBJECT_UNKNOWN = "unknown"


class MgmtController(ManagedObject):
    """This is MgmtController class."""

    consts = MgmtControllerConsts()
    naming_props = set([])

    mo_meta = MoMeta("MgmtController", "mgmtController", "mgmt", VersionMeta.Version101e, "InputOutput", 0x7f, [], ["admin", "ls-compute", "ls-config", "ls-network", "ls-server"], [u'adaptorUnit', u'computeBlade', u'computeBoardController', u'computeExtBoard', u'computeRackUnit', u'computeServerUnit', u'equipmentChassis', u'equipmentFex', u'equipmentIOCard', u'equipmentSharedIOModule', u'equipmentSwitchIOCard', u'networkElement', u'storageController', u'topSystem'], [u'cimcvmediaActualMountList', u'eventInst', u'fabricLocale', u'faultInst', u'firmwareBootDefinition', u'firmwareRunning', u'firmwareUpdatable', u'mgmtCimcSecureBoot', u'mgmtConnection', u'mgmtControllerFsm', u'mgmtControllerFsmTask', u'mgmtHealthStatus', u'mgmtIf', u'mgmtInterface', u'mgmtProfDerivedInterface', u'sysdebugMEpLog', u'vnicIpV4PooledAddr', u'vnicIpV4ProfDerivedAddr', u'vnicIpV4StaticAddr'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "desired_maintenance_mode": MoPropertyMeta("desired_maintenance_mode", "desiredMaintenanceMode", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lpc-reset", "normal"], []), 
        "dimm_blacklisting_oper_state": MoPropertyMeta("dimm_blacklisting_oper_state", "dimmBlacklistingOperState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled", "unknown", "unsupported"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "fsm_descr": MoPropertyMeta("fsm_descr", "fsmDescr", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_flags": MoPropertyMeta("fsm_flags", "fsmFlags", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]), 
        "fsm_prev": MoPropertyMeta("fsm_prev", "fsmPrev", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["ActivateAdaptorActivate", "ActivateAdaptorBegin", "ActivateAdaptorFail", "ActivateAdaptorPollActivateStatus", "ActivateAdaptorPowerOffServers", "ActivateAdaptorReset", "ActivateAdaptorServersPowerOffCompletion", "ActivateAdaptorSuccess", "ActivateBMCActivate", "ActivateBMCBegin", "ActivateBMCFail", "ActivateBMCReset", "ActivateBMCSuccess", "ActivateCMCActivate", "ActivateCMCBegin", "ActivateCMCFail", "ActivateCMCPollActivation", "ActivateCMCReset", "ActivateCMCSuccess", "ActivateIOMActivate", "ActivateIOMBegin", "ActivateIOMFail", "ActivateIOMReset", "ActivateIOMSuccess", "ExtMgmtIfConfigBegin", "ExtMgmtIfConfigFail", "ExtMgmtIfConfigPrimary", "ExtMgmtIfConfigSecondary", "ExtMgmtIfConfigSuccess", "ExtMgmtInterfaceConfigActive", "ExtMgmtInterfaceConfigBegin", "ExtMgmtInterfaceConfigCIMCVlanCfgLocal", "ExtMgmtInterfaceConfigCIMCVlanCfgPeer", "ExtMgmtInterfaceConfigCMCVlanCfg", "ExtMgmtInterfaceConfigCMCVlanCfgPeer", "ExtMgmtInterfaceConfigFail", "ExtMgmtInterfaceConfigSuccess", "LockConfigBegin", "LockConfigFail", "LockConfigPowerButtonLockConfig", "LockConfigSuccess", "OnlineBegin", "OnlineBmcConfigureConnLocal", "OnlineBmcConfigureConnPeer", "OnlineFail", "OnlineSuccess", "OnlineSwConfigureConnLocal", "OnlineSwConfigureConnPeer", "PowerBudgetReclaimConfigBegin", "PowerBudgetReclaimConfigFail", "PowerBudgetReclaimConfigPowerOffReclaim", "PowerBudgetReclaimConfigPowerOffWait", "PowerBudgetReclaimConfigSuccess", "RegistryConfigBegin", "RegistryConfigFail", "RegistryConfigRemove", "RegistryConfigSuccess", "SysConfigBegin", "SysConfigFail", "SysConfigPrimary", "SysConfigSecondary", "SysConfigSuccess", "UpdateAdaptorBegin", "UpdateAdaptorFail", "UpdateAdaptorPollUpdateStatus", "UpdateAdaptorSuccess", "UpdateAdaptorUpdateRequest", "UpdateBMCBegin", "UpdateBMCFail", "UpdateBMCPollUpdateStatus", "UpdateBMCSuccess", "UpdateBMCUpdateRequest", "UpdateBoardControllerBegin", "UpdateBoardControllerFail", "UpdateBoardControllerPollUpdateStatus", "UpdateBoardControllerPowerOffServers", "UpdateBoardControllerPrepareForUpdate", "UpdateBoardControllerServersPowerOffCompletion", "UpdateBoardControllerSuccess", "UpdateBoardControllerUpdateRequest", "UpdateCMCBegin", "UpdateCMCFail", "UpdateCMCPollUpdateStatus", "UpdateCMCSuccess", "UpdateCMCUpdateRequest", "UpdateIOMBegin", "UpdateIOMCopyIOMImgToSub", "UpdateIOMCopyImgFromRep", "UpdateIOMFail", "UpdateIOMPollUpdateStatus", "UpdateIOMSuccess", "UpdateIOMUpdateRequest", "UpdateRaidControllerActivate", "UpdateRaidControllerBegin", "UpdateRaidControllerFail", "UpdateRaidControllerPollActivation", "UpdateRaidControllerPollUpdateStatus", "UpdateRaidControllerPowerOffServers", "UpdateRaidControllerServersPowerOffCompletion", "UpdateRaidControllerSuccess", "UpdateRaidControllerUpdateRequest", "UpdateSwitchBegin", "UpdateSwitchCopyToLocal", "UpdateSwitchCopyToPeer", "UpdateSwitchFail", "UpdateSwitchResetLocal", "UpdateSwitchResetRemote", "UpdateSwitchSuccess", "UpdateSwitchUpdateLocal", "UpdateSwitchUpdateRemote", "UpdateSwitchVerifyLocal", "UpdateSwitchVerifyRemote", "UpdateUCSManagerBegin", "UpdateUCSManagerCopyExtToLocal", "UpdateUCSManagerCopyExtToPeer", "UpdateUCSManagerExecute", "UpdateUCSManagerFail", "UpdateUCSManagerStart", "UpdateUCSManagerSuccess", "nop"], []), 
        "fsm_progr": MoPropertyMeta("fsm_progr", "fsmProgr", "byte", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]), 
        "fsm_rmt_inv_err_code": MoPropertyMeta("fsm_rmt_inv_err_code", "fsmRmtInvErrCode", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["ERR-2fa-auth-retry", "ERR-ACTIVATE-failed", "ERR-ACTIVATE-in-progress", "ERR-ACTIVATE-retry", "ERR-BIOS-TOKENS-OLD-BIOS", "ERR-BIOS-TOKENS-OLD-CIMC", "ERR-BIOS-network-boot-order-not-found", "ERR-BOARDCTRLUPDATE-ignore", "ERR-DIAG-cancelled", "ERR-DIAG-fsm-restarted", "ERR-DIAG-test-failed", "ERR-DNLD-authentication-failure", "ERR-DNLD-hostkey-mismatch", "ERR-DNLD-invalid-image", "ERR-DNLD-no-file", "ERR-DNLD-no-space", "ERR-DNLD-usb-unmounted", "ERR-DNS-delete-error", "ERR-DNS-get-error", "ERR-DNS-set-error", "ERR-Diagnostics-in-progress", "ERR-Diagnostics-memtest-in-progress", "ERR-Diagnostics-network-in-progress", "ERR-FILTER-illegal-format", "ERR-FSM-no-such-state", "ERR-HOST-fru-identity-mismatch", "ERR-HTTP-set-error", "ERR-HTTPS-set-error", "ERR-IBMC-analyze-results", "ERR-IBMC-connect-error", "ERR-IBMC-connector-info-retrieval-error", "ERR-IBMC-fru-retrieval-error", "ERR-IBMC-invalid-end-point-config", "ERR-IBMC-results-not-ready", "ERR-MAX-subscriptions-allowed-error", "ERR-MO-CONFIG-child-object-cant-be-configured", "ERR-MO-META-no-such-object-class", "ERR-MO-PROPERTY-no-such-property", "ERR-MO-PROPERTY-value-out-of-range", "ERR-MO-access-denied", "ERR-MO-deletion-rule-violation", "ERR-MO-duplicate-object", "ERR-MO-illegal-containment", "ERR-MO-illegal-creation", "ERR-MO-illegal-iterator-state", "ERR-MO-illegal-object-lifecycle-transition", "ERR-MO-naming-rule-violation", "ERR-MO-object-not-found", "ERR-MO-resource-allocation", "ERR-NTP-delete-error", "ERR-NTP-get-error", "ERR-NTP-set-error", "ERR-POWER-CAP-UNSUPPORTED", "ERR-POWER-PROFILE-IN-PROGRESS", "ERR-SERVER-mis-connect", "ERR-SWITCH-invalid-if-config", "ERR-TOKEN-request-denied", "ERR-UNABLE-TO-FETCH-BIOS-SETTINGS", "ERR-UPDATE-failed", "ERR-UPDATE-in-progress", "ERR-UPDATE-retry", "ERR-aaa-config-modify-error", "ERR-acct-realm-set-error", "ERR-admin-passwd-set", "ERR-auth-issue", "ERR-auth-realm-get-error", "ERR-auth-realm-set-error", "ERR-authentication", "ERR-authorization-required", "ERR-cli-session-limit-reached", "ERR-create-keyring", "ERR-create-locale", "ERR-create-role", "ERR-create-tp", "ERR-create-user", "ERR-delete-locale", "ERR-delete-role", "ERR-delete-session", "ERR-delete-user", "ERR-downgrade-fail", "ERR-efi-Diagnostics--in-progress", "ERR-enable-mgmt-conn", "ERR-ep-set-error", "ERR-get-max-http-user-sessions", "ERR-http-initializing", "ERR-insufficiently-equipped", "ERR-internal-error", "ERR-ldap-delete-error", "ERR-ldap-get-error", "ERR-ldap-group-modify-error", "ERR-ldap-group-set-error", "ERR-ldap-set-error", "ERR-locale-set-error", "ERR-max-userid-sessions-reached", "ERR-missing-method", "ERR-modify-locale", "ERR-modify-role", "ERR-modify-user", "ERR-modify-user-locale", "ERR-modify-user-role", "ERR-provider-group-modify-error", "ERR-provider-group-set-error", "ERR-radius-get-error", "ERR-radius-global-set-error", "ERR-radius-group-set-error", "ERR-radius-set-error", "ERR-request-timeout", "ERR-reset-adapter", "ERR-role-set-error", "ERR-secondary-node", "ERR-service-not-ready", "ERR-session-cache-full", "ERR-session-not-found", "ERR-set-network", "ERR-set-password-strength-check", "ERR-set-port-channel", "ERR-store-pre-login-banner-msg", "ERR-tacacs-enable-error", "ERR-tacacs-global-set-error", "ERR-tacacs-group-set-error", "ERR-tacacs-plus-get-error", "ERR-tacacs-set-error", "ERR-test-error-1", "ERR-test-error-2", "ERR-timezone-set-error", "ERR-user-account-expired", "ERR-user-set-error", "ERR-xml-parse-error", "none"], ["0-4294967295"]), 
        "fsm_rmt_inv_err_descr": MoPropertyMeta("fsm_rmt_inv_err_descr", "fsmRmtInvErrDescr", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], []), 
        "fsm_rmt_inv_rslt": MoPropertyMeta("fsm_rmt_inv_rslt", "fsmRmtInvRslt", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, r"""((defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout),){0,32}(defaultValue|not-applicable|resource-unavailable|service-unavailable|intermittent-error|sw-defect|service-not-implemented-ignore|extend-timeout|capability-not-implemented-failure|illegal-fru|end-point-unavailable|failure|resource-capacity-exceeded|service-protocol-error|fw-defect|service-not-implemented-fail|task-reset|unidentified-fail|capability-not-supported|end-point-failed|fru-state-indeterminate|resource-dependency|fru-identity-indeterminate|internal-error|hw-defect|service-not-supported|fru-not-supported|end-point-protocol-error|capability-unavailable|fru-not-ready|capability-not-implemented-ignore|fru-info-malformed|timeout){0,1}""", [], []), 
        "fsm_stage_descr": MoPropertyMeta("fsm_stage_descr", "fsmStageDescr", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "fsm_stamp": MoPropertyMeta("fsm_stamp", "fsmStamp", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["never"], []), 
        "fsm_status": MoPropertyMeta("fsm_status", "fsmStatus", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["ActivateAdaptorActivate", "ActivateAdaptorBegin", "ActivateAdaptorFail", "ActivateAdaptorPollActivateStatus", "ActivateAdaptorPowerOffServers", "ActivateAdaptorReset", "ActivateAdaptorServersPowerOffCompletion", "ActivateAdaptorSuccess", "ActivateBMCActivate", "ActivateBMCBegin", "ActivateBMCFail", "ActivateBMCReset", "ActivateBMCSuccess", "ActivateCMCActivate", "ActivateCMCBegin", "ActivateCMCFail", "ActivateCMCPollActivation", "ActivateCMCReset", "ActivateCMCSuccess", "ActivateIOMActivate", "ActivateIOMBegin", "ActivateIOMFail", "ActivateIOMReset", "ActivateIOMSuccess", "ExtMgmtIfConfigBegin", "ExtMgmtIfConfigFail", "ExtMgmtIfConfigPrimary", "ExtMgmtIfConfigSecondary", "ExtMgmtIfConfigSuccess", "ExtMgmtInterfaceConfigActive", "ExtMgmtInterfaceConfigBegin", "ExtMgmtInterfaceConfigCIMCVlanCfgLocal", "ExtMgmtInterfaceConfigCIMCVlanCfgPeer", "ExtMgmtInterfaceConfigCMCVlanCfg", "ExtMgmtInterfaceConfigCMCVlanCfgPeer", "ExtMgmtInterfaceConfigFail", "ExtMgmtInterfaceConfigSuccess", "LockConfigBegin", "LockConfigFail", "LockConfigPowerButtonLockConfig", "LockConfigSuccess", "OnlineBegin", "OnlineBmcConfigureConnLocal", "OnlineBmcConfigureConnPeer", "OnlineFail", "OnlineSuccess", "OnlineSwConfigureConnLocal", "OnlineSwConfigureConnPeer", "PowerBudgetReclaimConfigBegin", "PowerBudgetReclaimConfigFail", "PowerBudgetReclaimConfigPowerOffReclaim", "PowerBudgetReclaimConfigPowerOffWait", "PowerBudgetReclaimConfigSuccess", "RegistryConfigBegin", "RegistryConfigFail", "RegistryConfigRemove", "RegistryConfigSuccess", "SysConfigBegin", "SysConfigFail", "SysConfigPrimary", "SysConfigSecondary", "SysConfigSuccess", "UpdateAdaptorBegin", "UpdateAdaptorFail", "UpdateAdaptorPollUpdateStatus", "UpdateAdaptorSuccess", "UpdateAdaptorUpdateRequest", "UpdateBMCBegin", "UpdateBMCFail", "UpdateBMCPollUpdateStatus", "UpdateBMCSuccess", "UpdateBMCUpdateRequest", "UpdateBoardControllerBegin", "UpdateBoardControllerFail", "UpdateBoardControllerPollUpdateStatus", "UpdateBoardControllerPowerOffServers", "UpdateBoardControllerPrepareForUpdate", "UpdateBoardControllerServersPowerOffCompletion", "UpdateBoardControllerSuccess", "UpdateBoardControllerUpdateRequest", "UpdateCMCBegin", "UpdateCMCFail", "UpdateCMCPollUpdateStatus", "UpdateCMCSuccess", "UpdateCMCUpdateRequest", "UpdateIOMBegin", "UpdateIOMCopyIOMImgToSub", "UpdateIOMCopyImgFromRep", "UpdateIOMFail", "UpdateIOMPollUpdateStatus", "UpdateIOMSuccess", "UpdateIOMUpdateRequest", "UpdateRaidControllerActivate", "UpdateRaidControllerBegin", "UpdateRaidControllerFail", "UpdateRaidControllerPollActivation", "UpdateRaidControllerPollUpdateStatus", "UpdateRaidControllerPowerOffServers", "UpdateRaidControllerServersPowerOffCompletion", "UpdateRaidControllerSuccess", "UpdateRaidControllerUpdateRequest", "UpdateSwitchBegin", "UpdateSwitchCopyToLocal", "UpdateSwitchCopyToPeer", "UpdateSwitchFail", "UpdateSwitchResetLocal", "UpdateSwitchResetRemote", "UpdateSwitchSuccess", "UpdateSwitchUpdateLocal", "UpdateSwitchUpdateRemote", "UpdateSwitchVerifyLocal", "UpdateSwitchVerifyRemote", "UpdateUCSManagerBegin", "UpdateUCSManagerCopyExtToLocal", "UpdateUCSManagerCopyExtToPeer", "UpdateUCSManagerExecute", "UpdateUCSManagerFail", "UpdateUCSManagerStart", "UpdateUCSManagerSuccess", "nop"], []), 
        "fsm_try": MoPropertyMeta("fsm_try", "fsmTry", "byte", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "guid": MoPropertyMeta("guid", "guid", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version251a, MoPropertyMeta.NAMING, 0x8, None, None, None, ["A", "B", "NONE"], []), 
        "last_reboot_reason": MoPropertyMeta("last_reboot_reason", "lastRebootReason", "string", VersionMeta.Version226a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_conn": MoPropertyMeta("oper_conn", "operConn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "power_fan_speed_policy_supported": MoPropertyMeta("power_fan_speed_policy_supported", "powerFanSpeedPolicySupported", "string", VersionMeta.Version226a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "storage_oob_config_supported": MoPropertyMeta("storage_oob_config_supported", "storageOobConfigSupported", "string", VersionMeta.Version224a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "storage_oob_interface_supported": MoPropertyMeta("storage_oob_interface_supported", "storageOobInterfaceSupported", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "storage_subsystem_state": MoPropertyMeta("storage_subsystem_state", "storageSubsystemState", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["initialized", "initializing", "uninitialized", "unknown", "unsupported"], []), 
        "subject": MoPropertyMeta("subject", "subject", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["adaptor", "blade", "board-controller", "chassis", "cmc", "iocard", "server-unit", "switch", "system", "unknown"], []), 
        "supported_capability": MoPropertyMeta("supported_capability", "supportedCapability", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|modify-maintenance-mode),){0,2}(defaultValue|none|modify-maintenance-mode){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "desiredMaintenanceMode": "desired_maintenance_mode", 
        "dimmBlacklistingOperState": "dimm_blacklisting_oper_state", 
        "dn": "dn", 
        "fsmDescr": "fsm_descr", 
        "fsmFlags": "fsm_flags", 
        "fsmPrev": "fsm_prev", 
        "fsmProgr": "fsm_progr", 
        "fsmRmtInvErrCode": "fsm_rmt_inv_err_code", 
        "fsmRmtInvErrDescr": "fsm_rmt_inv_err_descr", 
        "fsmRmtInvRslt": "fsm_rmt_inv_rslt", 
        "fsmStageDescr": "fsm_stage_descr", 
        "fsmStamp": "fsm_stamp", 
        "fsmStatus": "fsm_status", 
        "fsmTry": "fsm_try", 
        "guid": "guid", 
        "id": "id", 
        "lastRebootReason": "last_reboot_reason", 
        "model": "model", 
        "operConn": "oper_conn", 
        "powerFanSpeedPolicySupported": "power_fan_speed_policy_supported", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "status": "status", 
        "storageOobConfigSupported": "storage_oob_config_supported", 
        "storageOobInterfaceSupported": "storage_oob_interface_supported", 
        "storageSubsystemState": "storage_subsystem_state", 
        "subject": "subject", 
        "supportedCapability": "supported_capability", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.desired_maintenance_mode = None
        self.dimm_blacklisting_oper_state = None
        self.fsm_descr = None
        self.fsm_flags = None
        self.fsm_prev = None
        self.fsm_progr = None
        self.fsm_rmt_inv_err_code = None
        self.fsm_rmt_inv_err_descr = None
        self.fsm_rmt_inv_rslt = None
        self.fsm_stage_descr = None
        self.fsm_stamp = None
        self.fsm_status = None
        self.fsm_try = None
        self.guid = None
        self.id = None
        self.last_reboot_reason = None
        self.model = None
        self.oper_conn = None
        self.power_fan_speed_policy_supported = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.status = None
        self.storage_oob_config_supported = None
        self.storage_oob_interface_supported = None
        self.storage_subsystem_state = None
        self.subject = None
        self.supported_capability = None
        self.vendor = None

        ManagedObject.__init__(self, "MgmtController", parent_mo_or_dn, **kwargs)
