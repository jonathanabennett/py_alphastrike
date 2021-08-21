import uuid


class RecordSheet:
    def __init__(
        self,
        name,
        pv,
        u_type,
        size,
        tmm,
        move_distance,
        move_type,
        role,
        skill,
        damage,
        ov,
        armor,
        structure,
        specials,
        uuid=uuid.uuid4(),
        cur_armor=None,
        cur_structure=None,
        heat=0,
        crits=[],
    ):
        self.name = name
        self.pv = pv
        self.u_type = u_type
        self.size = size
        self.tmm = tmm
        self.mv = move_distance
        self.move_type = move_type
        self.role = role
        self.skill = skill
        self.damage = damage
        self.ov = ov
        self.armor = armor
        self.structure = structure
        self.cur_armor = cur_armor or armor
        self.cur_structure = cur_structure or structure
        self.specials = specials
        self.uuid = uuid
        self.heat = heat
        self.crits = crits
