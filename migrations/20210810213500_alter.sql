ALTER TABLE public.purchases ADD "size" varchar NOT NULL;
ALTER TABLE public.purchases ADD color varchar NOT NULL;
ALTER TABLE public.products ADD size_available _text NOT NULL DEFAULT '{S, M, B}';
ALTER TABLE public.products ADD color_available _text NOT NULL DEFAULT '{"black", "red"}';

ALTER TABLE public.purchases ADD status varchar NOT NULL DEFAULT 'pending_payment';
ALTER TABLE public.purchases ADD created_at timestamptz NOT NULL DEFAULT now();
ALTER TABLE public.purchases ADD updated_at timestamptz NOT NULL DEFAULT now();
ALTER TABLE public.purchases ADD canceled_at timestamptz NULL;
ALTER TABLE public.purchases ADD reason text NULL;

ALTER TABLE public.purchases ADD payment_type varchar NULL;
ALTER TABLE public.purchases ADD delivery_forecast timestamptz NULL;
ALTER TABLE public.purchases ADD purchase_code int8 NOT NULL;

ALTER TABLE public.looks ADD category varchar NOT NULL;