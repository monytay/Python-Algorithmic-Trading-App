from django.contrib import admin
from portfolio.models import Portfolio, Position, Trade, PerformanceMetric

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'current_cash', 'total_value', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Position)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'stock', 'quantity', 'average_cost', 'current_value', 'unrealized_pnl')
    list_filter = ('portfolio', 'last_updated')
    search_fields = ('portfolio_name', 'stock_ticker')
    readonly_fields = ('created_at', 'last_updated')

@admin.register(Trade)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'stock','trade_type', 'quantity', 'price', 'status', 'created_at')
    list_filter = ('trade_type', 'status', 'created_at', 'portfolio')
    readonly_fields = ('created_at', 'submitted_at')
    date_hierarchy = "created_at"

@admin.register(PerformanceMetric)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'date', 'total_value', 'daily_return', 'total_trades', 'winning_trades', 'losing_trades', 'cummulative_return')
    list_filter = ('portfolio', 'date')
    readonly_fields = ('created_at',)

