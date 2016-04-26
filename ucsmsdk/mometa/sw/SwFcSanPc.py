"""This module contains the general information for SwFcSanPc ManagedObject."""
import sys, os

from ...ucsmo import ManagedObject
from ...ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwFcSanPcConsts():
    ADMIN_SPEED_16GBPS = "16gbps"
    ADMIN_SPEED_1GBPS = "1gbps"
    ADMIN_SPEED_2GBPS = "2gbps"
    ADMIN_SPEED_4GBPS = "4gbps"
    ADMIN_SPEED_8GBPS = "8gbps"
    ADMIN_SPEED_AUTO = "auto"
    ADMIN_SPEED_INDETERMINATE = "indeterminate"
    ADMIN_STATE_DISABLED = "disabled"
    ADMIN_STATE_ENABLED = "enabled"
    IF_ROLE_DIAG = "diag"
    IF_ROLE_FCOE_NAS_STORAGE = "fcoe-nas-storage"
    IF_ROLE_FCOE_STORAGE = "fcoe-storage"
    IF_ROLE_FCOE_UPLINK = "fcoe-uplink"
    IF_ROLE_MGMT = "mgmt"
    IF_ROLE_MONITOR = "monitor"
    IF_ROLE_NAS_STORAGE = "nas-storage"
    IF_ROLE_NETWORK = "network"
    IF_ROLE_NETWORK_FCOE_UPLINK = "network-fcoe-uplink"
    IF_ROLE_SERVER = "server"
    IF_ROLE_SERVICE = "service"
    IF_ROLE_STORAGE = "storage"
    IF_ROLE_UNKNOWN = "unknown"
    IF_TYPE_AGGREGATION = "aggregation"
    IF_TYPE_PHYSICAL = "physical"
    IF_TYPE_UNKNOWN = "unknown"
    IF_TYPE_VIRTUAL = "virtual"
    MON_TRAF_DIR_BOTH = "both"
    MON_TRAF_DIR_RX = "rx"
    MON_TRAF_DIR_TX = "tx"
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class SwFcSanPc(ManagedObject):
    """This is SwFcSanPc class."""

    consts = SwFcSanPcConsts()
    naming_props = set([u'portId'])

    mo_meta = MoMeta("SwFcSanPc", "swFcSanPc", "pc-[port_id]", VersionMeta.Version141i, "InputOutput", 0xff, [], ["read-only"], [u'swFcMon', u'swFcSanBorder'], [], ["Get"])

    prop_meta = {
        "admin_speed": MoPropertyMeta("admin_speed", "adminSpeed", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["16gbps", "1gbps", "2gbps", "4gbps", "8gbps", "auto", "indeterminate"], []), 
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, ["disabled", "enabled"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x4, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "if_role": MoPropertyMeta("if_role", "ifRole", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["diag", "fcoe-nas-storage", "fcoe-storage", "fcoe-uplink", "mgmt", "monitor", "nas-storage", "network", "network-fcoe-uplink", "server", "service", "storage", "unknown"], []), 
        "if_type": MoPropertyMeta("if_type", "ifType", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], []), 
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []), 
        "mon_traf_dir": MoPropertyMeta("mon_traf_dir", "monTrafDir", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["both", "rx", "tx"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "pc_id": MoPropertyMeta("pc_id", "pcId", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "port_id": MoPropertyMeta("port_id", "portId", "uint", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x20, None, None, None, [], []), 
        "port_vsan_id": MoPropertyMeta("port_vsan_id", "portVsanId", "uint", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-4093"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []), 
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []), 
    }

    prop_map = {
        "adminSpeed": "admin_speed", 
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "ifRole": "if_role", 
        "ifType": "if_type", 
        "locale": "locale", 
        "monTrafDir": "mon_traf_dir", 
        "name": "name", 
        "pcId": "pc_id", 
        "peerDn": "peer_dn", 
        "portId": "port_id", 
        "portVsanId": "port_vsan_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, port_id, **kwargs):
        self._dirty_mask = 0
        self.port_id = port_id
        self.admin_speed = None
        self.admin_state = None
        self.child_action = None
        self.ep_dn = None
        self.if_role = None
        self.if_type = None
        self.locale = None
        self.mon_traf_dir = None
        self.name = None
        self.pc_id = None
        self.peer_dn = None
        self.port_vsan_id = None
        self.sacl = None
        self.status = None
        self.switch_id = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "SwFcSanPc", parent_mo_or_dn, **kwargs)
