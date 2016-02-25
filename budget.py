from Entity import Entity, EntityListField, EntityField,  undef
from datetime import datetime


class Transaction(Entity):
    Fields= dict(
            accepted=EntityField(None),
            amount=EntityField(None),
            cash_amount=EntityField(0),
            check_number=EntityField(None),
            cleared=EntityField('UnCleared'),
            credit_amount=EntityField(0),
            date=EntityField(datetime.now().strftime('%Y-%m-%d')),
            date_entered_from_schedule=EntityField(None),
            entities_account_id=EntityField(None),
            entities_payee_id=EntityField(None),
            entities_scheduled_transaction_id=EntityField(None),
            entities_subcategory_id=EntityField(None),
            flag=EntityField(None),
            imported_date=EntityField(None),
            imported_payee=EntityField(None),
            is_tombstone=EntityField(False),
            matched_transaction_id=EntityField(None),
            memo=EntityField(None),
            source=EntityField(None),
            transfer_account_id=EntityField(None),
            transfer_subtransaction_id=EntityField(None),
            transfer_transaction_id=EntityField(None),
            ynab_id=EntityField(None)
        )


class MasterCategory(Entity):
    Fields= dict(
            deletable=EntityField(None),
            internal_name=EntityField(None),
            is_hidden=EntityField(None),
            is_tombstone=EntityField(False),
            name=EntityField(None),
            note=EntityField(None),
            sortable_index=EntityField(None)
        )


class Setting(Entity):
    Fields= dict(
            setting_name=EntityField(None),
            setting_value=EntityField(None)
        )


class MonthlyBudgetCalculation(Entity):
    Fields= dict(
            additional_to_be_budgeted=EntityField(None),
            age_of_money=EntityField(None),
            available_to_budget=EntityField(None),
            balance=EntityField(None),
            budgeted=EntityField(None),
            calculation_notes=EntityField(None),
            cash_outflows=EntityField(None),
            credit_outflows=EntityField(None),
            deferred_income=EntityField(None),
            entities_monthly_budget_id=EntityField(None),
            hidden_balance=EntityField(None),
            hidden_budgeted=EntityField(None),
            hidden_cash_outflows=EntityField(None),
            hidden_credit_outflows=EntityField(None),
            immediate_income=EntityField(None),
            is_tombstone=EntityField(False),
            over_spent=EntityField(None),
            previous_income=EntityField(None),
            uncategorized_balance=EntityField(None),
            uncategorized_cash_outflows=EntityField(None),
            uncategorized_credit_outflows=EntityField(None)
        )


class AccountMapping(Entity):
    Fields= dict(
            date_sequence=EntityField(None),
            entities_account_id=EntityField(None),
            hash=EntityField(None),
            is_tombstone=EntityField(False),
            salt=EntityField(None),
            shortened_account_id=EntityField(None),
            should_flip_payees_memos=EntityField(None),
            should_import_memos=EntityField(None),
            skip_import=EntityField(None)
        )


class Subtransaction(Entity):
    Fields= dict(
            amount=EntityField(None),
            cash_amount=EntityField(None),
            check_number=EntityField(None),
            credit_amount=EntityField(None),
            entities_payee_id=EntityField(None),
            entities_subcategory_id=EntityField(None),
            entities_transaction_id=EntityField(None),
            is_tombstone=EntityField(False),
            memo=EntityField(None),
            sortable_index=EntityField(None),
            transfer_account_id=EntityField(None),
            transfer_transaction_id=EntityField(None)
        )


class ScheduledSubtransaction(Entity):
    Fields= dict(
            amount=EntityField(None),
            entities_payee_id=EntityField(None),
            entities_scheduled_transaction_id=EntityField(None),
            entities_subcategory_id=EntityField(None),
            is_tombstone=EntityField(False),
            memo=EntityField(None),
            sortable_index=EntityField(None),
            transfer_account_id=EntityField(None)
        )


class MonthlyBudget(Entity):
    Fields= dict(
            is_tombstone=EntityField(False),
            month=EntityField(None),
            note=EntityField(None)
        )


class Subcategory(Entity):
    Fields= dict(
            entities_account_id=EntityField(None),
            entities_master_category_id=EntityField(None),
            goal_creation_month=EntityField(None),
            goal_type=EntityField(None),
            internal_name=EntityField(None),
            is_hidden=EntityField(None),
            is_tombstone=EntityField(False),
            monthly_funding=EntityField(None),
            name=EntityField(None),
            note=EntityField(None),
            sortable_index=EntityField(None),
            target_balance=EntityField(None),
            target_balance_month=EntityField(None),
            type=EntityField(None)
        )


class PayeeLocation(Entity):
    Fields= dict(
            entities_payee_id=EntityField(None),
            is_tombstone=EntityField(False),
            latitude=EntityField(None),
            longitude=EntityField(None)
        )


class AccountCalculation(Entity):
    Fields= dict(
            cleared_balance=EntityField(None),
            entities_account_id=EntityField(None),
            error_count=EntityField(None),
            info_count=EntityField(None),
            is_tombstone=EntityField(False),
            transaction_count=EntityField(None),
            uncleared_balance=EntityField(None),
            warning_count=EntityField(None)
        )


class MonthlyAccountCalculation(Entity):
    Fields= dict(
            cleared_balance=EntityField(None),
            entities_account_id=EntityField(None),
            error_count=EntityField(None),
            info_count=EntityField(None),
            is_tombstone=EntityField(False),
            month=EntityField(None),
            transaction_count=EntityField(None),
            uncleared_balance=EntityField(None),
            warning_count=EntityField(None)
        )


class MonthlySubcategoryBudgetCalculation(Entity):
    Fields= dict(
            all_spending=EntityField(None),
            all_spending_since_last_payment=EntityField(None),
            balance=EntityField(None),
            balance_previous_month=EntityField(None),
            budgeted_average=EntityField(None),
            budgeted_cash_outflows=EntityField(None),
            budgeted_credit_outflows=EntityField(None),
            budgeted_previous_month=EntityField(None),
            budgeted_spending=EntityField(None),
            cash_outflows=EntityField(None),
            credit_outflows=EntityField(None),
            entities_monthly_subcategory_budget_id=EntityField(None),
            goal_expected_completion=EntityField(None),
            goal_overall_funded=EntityField(None),
            goal_overall_left=EntityField(None),
            goal_target=EntityField(None),
            goal_under_funded=EntityField(None),
            is_tombstone=EntityField(False),
            overspending_affects_buffer=EntityField(None),
            payment_average=EntityField(None),
            payment_previous_month=EntityField(None),
            spent_average=EntityField(None),
            spent_previous_month=EntityField(None),
            unbudgeted_cash_outflows=EntityField(None),
            unbudgeted_credit_outflows=EntityField(None),
            upcoming_transactions=EntityField(None)
        )


class ScheduledTransaction(Entity):
    Fields= dict(
            amount=EntityField(None),
            date=EntityField(None),
            entities_account_id=EntityField(None),
            entities_payee_id=EntityField(None),
            entities_subcategory_id=EntityField(None),
            flag=EntityField(None),
            frequency=EntityField(None),
            is_tombstone=EntityField(False),
            memo=EntityField(None),
            transfer_account_id=EntityField(None),
            upcoming_instances=EntityField(None)
        )


class Payee(Entity):
    Fields= dict(
            auto_fill_amount=EntityField(None),
            auto_fill_amount_enabled=EntityField(None),
            auto_fill_memo=EntityField(None),
            auto_fill_memo_enabled=EntityField(None),
            auto_fill_subcategory_enabled=EntityField(None),
            auto_fill_subcategory_id=EntityField(None),
            enabled=EntityField(None),
            entities_account_id=EntityField(None),
            internal_name=EntityField(None),
            is_tombstone=EntityField(False),
            name=EntityField(None),
            rename_on_import_enabled=EntityField(None)
        )


class MonthlySubcategoryBudget(Entity):
    Fields= dict(
            budgeted=EntityField(None),
            entities_monthly_budget_id=EntityField(None),
            entities_subcategory_id=EntityField(None),
            is_tombstone=EntityField(False),
            note=EntityField(None),
            overspending_handling=EntityField(None)
        )


class TransactionGroup(Entity):
    Fields= dict(
            be_transaction=EntityField(None),
            be_subtransactions=EntityField(None),
            be_matched_transaction=EntityField(None)
        )


class PayeeRenameCondition(Entity):
    Fields= dict(
            entities_payee_id=EntityField(None),
            is_tombstone=EntityField(False),
            operand=EntityField(None),
            operator=EntityField(None)
        )


class Account(Entity):
    Fields= dict(
            account_name=EntityField(None),
            account_type=EntityField(None),
            direct_connect_account_id=EntityField(undef),
            direct_connect_enabled=EntityField(None),
            direct_connect_institution_id=EntityField(undef),
            hidden=EntityField(None),
            is_tombstone=EntityField(False),
            last_entered_check_number=EntityField(None),
            last_imported_at=EntityField(undef),
            last_imported_error_code=EntityField(undef),
            last_reconciled_balance=EntityField(None),
            last_reconciled_date=EntityField(None),
            note=EntityField(None),
            on_budget=EntityField(None),
            sortable_index=EntityField(None)
        )



