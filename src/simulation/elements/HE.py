#include "simulation/ElementCommon.h"

void Element::Element_HE()
{
	Identifier = "DEFAULT_PT_HE";
	Name = "HE";
	Colour = 0xDEF9FF_rgb;
	MenuVisible = 1;
	MenuSection = SC_GAS;
	Enabled = 1;

	Advection = 3.0f;
	AirDrag = 0.005f * CFDS;
	AirLoss = 0.995f;
	Loss = 0.40f;
	Collision = -0.1f;
	Gravity = -0.15f;
	Diffusion = 10.0f;
	HotAir = 0.000f	* CFDS;
	Falldown = 0;

	Flammable = 0;
	Explosive = 0;
	Meltable = 0;
	Hardness = 0;

	Weight = 0.8;

  Temperature = 10.0f;
	HeatConduct = 200;
	Description = "Helium. Liquifies near absolute zero.";

	Properties = TYPE_GAS | PROP_NEUTPASS;

	LowPressure = IPL;
	LowPressureTransition = NT;
	HighPressure = IPH;
	HighPressureTransition = NT;
	LowTemperature = -200.0f;
	LowTemperatureTransition = PT_LNTG;
	HighTemperature = 6000.0f;
	HighTemperatureTransition = PT_FIRE;
}
