from tkinter import *
from record_sheet import RecordSheet

window = Tk()

locust = RecordSheet(
    "Locust", 18, "BM", 1, 3, 8, "w", "Scout", 4, [1, 1, 0], 0, 2, 2, []
)

window.title("Welcome to Alphastrike")

name_lbl = Label(window, text=locust.name, font=("Arial Bold", 24))
name_lbl.grid(column=0, row=0)

pv_lbl = Label(window, text=locust.pv)
pv_lbl.grid(column=1, row=0)

type_lbl = Label(window, text=f"Type: {locust.u_type}")
type_lbl.grid(column=0, row=1)

size_lbl = Label(window, text=f"Size: {locust.size}")
size_lbl.grid(column=1, row=1)
tmm_lbl = Label(window, text=f"TMM: {locust.tmm}")
tmm_lbl.grid(column=2, row=1)
mv_lbl = Label(window, text=f"Mv: {locust.mv}{locust.move_type}")
mv_lbl.grid(column=3, row=1)
role_lbl = Label(window, text=f"Role: {locust.role}")
role_lbl.grid(column=0, row=2)
skill_lbl = Label(window, text=f"Skill: {locust.skill}")
skill_lbl.grid(column=1, row=2)
damage_lbl = Label(
    window,
    text=f"DAMAGE\tS(+0){locust.damage[0]}\tM(+2){locust.damage[1]}\tL(+4){locust.damage[2]}",
)
damage_lbl.grid(column=0, row=3)
ov_lbl = Label(window, text=f"OV: {locust.ov}")
ov_lbl.grid(column=0, row=4)
heat_lbl = Label(window, text=f"Current Heat: {locust.heat}")
type_lbl.grid(column=1, row=4)
armor_lbl = Label(window, text=f"Armor: {locust.cur_armor}/{locust.armor}")
armor_lbl.grid(column=0, row=5)
structure_lbl = Label(
    window, text=f"Structure: {locust.cur_structure}/{locust.structure}"
)
structure_lbl.grid(column=0, row=6)
specials_lbl = Label(window, text=f"Type: {locust.specials}")
specials_lbl.grid(column=0, row=7)
crits_lbl = Label(window, text=f"Type: {locust.crits}")
crits_lbl.grid(column=0, row=8)

window.mainloop()
