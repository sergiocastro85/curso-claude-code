import { defineCollection, z } from 'astro:content';

const modulos = defineCollection({
  type: 'content',
  schema: z.object({
    numero: z.number(),
    titulo: z.string(),
    semana: z.number(),
    objetivo: z.string(),
    duracionMinutos: z.number().default(245),
    premium: z.boolean().default(false), // material extra solo para el kit
    fuentes: z.array(z.object({ titulo: z.string(), url: z.string().url() })),
    ogImage: z.string().optional(),
  }),
});

export const collections = { modulos };
