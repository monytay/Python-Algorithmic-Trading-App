from django.contrib import admin
from trading.models import Stock, PriceData, MomentumScore, TradingSignal, RebalanceEvent
@admin.register(Stock)
class TradingStock(admin.ModelAdmin):
    list_display = ('ticker', 'name', 'sector', 'is_active', 'created_at')
    list_filter = ('is_active', 'sector')
    search_fields = ('ticker', 'name')
    readonly_fields = ('created_at', 'updated_at')
# Register your models here.

@admin.register(PriceData)
class TradingAdmin(admin.ModelAdmin):
    list_display = ('stock', 'date', 'close', 'volume')
    list_filter = ('stock', 'date')
    search_fields = ('stock',)
    readonly_fields = ('created_at', 'date')
# Register your models here.

@admin.register(MomentumScore)
class TradingAdmin(admin.ModelAdmin):
    list_display = ('stock', 'calculation_date', 'momentum_score', 'rank', 'quintile', 'period_start', 'period_end', 'created_at')
    list_filter = ('stock', 'rank')
    search_fields = ('stock', 'calculation_date', 'momentum_score')
    readonly_fields = ('created_at', 'period_start', 'period_end')
# Register your models here.

@admin.register(TradingSignal)
class TradingAdmin(admin.ModelAdmin):
    list_display = ('stock', 'signal_date', 'signal_type', 'momentum_score', 'target_quantity', 'target_value', 'executed_at', 'created_at')
    list_filter = ('stock', 'signal_type')
    search_fields = ('stock', 'signal_date', 'signal_type')
    readonly_fields = ('created_at', 'signal_date', 'executed_at')
    pass

@admin.register(RebalanceEvent)
class TradingAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_stocks_analyzed', 'buy_signals_generated', 'sell_signals_generated', 'total_portfolio_value', 'execution_status', 'completed_at', 'created_at')
    list_filter = ('date', 'execution_status')
    search_fields = ('date',)
    readonly_fields = ('created_at', 'date', 'completed_at')
    pass