from django.contrib import admin
from trading.models import Stock, PriceData, MomentumScore, TradingSignal, RebalanceEvent
@admin.register(Stock)
class TradingStock(admin.ModelAdmin):
    pass
# Register your models here.

@admin.register(PriceData)
class TradingAdmin(admin.ModelAdmin):
    pass
# Register your models here.

@admin.register(MomentumScore)
class TradingAdmin(admin.ModelAdmin):
    pass
# Register your models here.

@admin.register(TradingSignal)
class TradingAdmin(admin.ModelAdmin):
    pass

@admin.register(RebalanceEvent)
class TradingAdmin(admin.ModelAdmin):
    pass